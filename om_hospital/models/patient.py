import datetime

from odoo import fields, api, models
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    # Based on the _name the table will get created inside Postgress
    # It will be hospital_patient instead of the ' . '
    _name = "hospital.patient"

    # Inheriting from "mail.thread" to add Chatter to a Form
    # Inheriting from "mail.activity.mixin" to add "activity_ids"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Patient"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', tracking=True)
    email = fields.Char(string='Email')

    # Array of Tuples.
    availableGenders = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    possibleStates = [
        ('billed', 'Billed'),
        ('sick', 'Sick'),
        ('treating', 'Treating'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ]

    availableDepartments = [
        ('brain', 'Brain'),
        ('heart', 'Heart')
    ]

    gender = fields.Selection(availableGenders, default='male')
    note = fields.Text(
        string='Description',
        groups='om_hospital.group_hospital_heart_doctor,'
        +
        'om_hospital.group_hospital_brain_doctor'
    )

    # These are the possible states for the Progress bar (Status bar).
    # Tracking param allows the current value to be tracked.
    state = fields.Selection(
        possibleStates,
        string="Status",
        tracking=True
    )

    department = fields.Selection(availableDepartments, string='Department')
    price = fields.Integer(string='Price')

    # Many2one Field is basically obtained from another place.
    # Many2one Fields r named (name)_id due to convention.
    # "res.partner" is currently unknown to me (res) = rest.
    # (partner) = which model to show from.
    responsible_id = fields.Many2one('res.partner', string="Responsible")
    #
    reference = fields.Char(
        string="Order Reference",
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: 'New'
    )

    # This function fires at the button press from the view.
    def ConfirmPayment(self):
        msg = 'Will you pay ' + str(self.price) + ' SAR?'
        # Here i am calling the action defined inside
        # Dialogue_box_view.xml and passing a context
        return {
            'name': 'Payment Confirmation',
            'type': 'ir.actions.act_window',
            'res_model': 'dialogue.box.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_prompt_msg': msg,
                'default_inv_id': self.associated_invoice_id,
            }
        }

    associated_invoice_id = fields.Integer()
    def TreatingButton(self):
        invoice = self.env['account.move'].search([('id', '=', self.associated_invoice_id)])
        if invoice.state == 'draft':
            ValidationError('Sorry, patient needs to pay the fees')
        elif invoice.state == 'posted':
            self.state = 'treating'
        else:
            ValidationError('something went wrong..?')

    def DoneButton(self):
        self.state = 'done'

    def CancelButton(self):
        self.state = 'cancel'

    # Overriding db record create method.
    @api.model
    def create(self, vals):
        vals['state'] = 'billed'
        price = 0

        if vals['department'] == 'brain':
            price = 5
        else:
            price = 10

        vals['price'] = price

        # TODO: Create an invoice for the patient with the price
        partner = self.env['res.partner'].search([('name', '=', 'bassam')])
        currency = self.env['res.currency'].search([('name', '=', 'SAR')])

        invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': partner.id,
            'invoice_date': datetime.date.today(),
            'invoice_line_ids': [("label", 0, {
                'name': 'examination',
                'quantity': 1,
                'price_unit': price,
                'tax_ids': [(6, 0, 0)],
            })]
        })

        vals['associated_invoice_id'] = invoice.id
        # if '@' not in vals['email']:
        # raise ValidationError('The Email Address is Incorrect')

        # if not self.ValidateEmail(vals['email']):
        # raise ValidationError('The Email Address Does not match any users')

        # create(vals) is for the chatter log message.
        # Setting note (description) field to new patient if its empty.
        vals['note'] = "New patient"

        if vals.get('reference', 'New') == 'New':
            vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient') or 'New'

        # vals will be the results entered during record creation.
        # super(ClassStructure, ActualClassWithData)
        return super(HospitalPatient, self).create(vals)

    # Hides the edit button if the user is a receptionist.
    # While allowing only for state cancellation.
    def check_access_rights(self, operation, raise_exception=True):
        not_allowed = self.env.user.has_group('om_hospital.group_hospital_receptionist')
        if operation == 'write' and not_allowed:
            return False
        return super(HospitalPatient, self).check_access_rights(operation, raise_exception)


    def ValidateEmail(self, emailString):
        usersList = self.env['res.users'].search([])
        for user in usersList:
            print(user.login)
            if user.login == emailString:
                return True
        return False
