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
    note = fields.Text(string='Description')

    # These are the possible states for the Progress bar (Status bar).
    # Tracking param allows the current value to be tracked.
    state = fields.Selection(
        possibleStates,
        string="Status",
        tracking=True
    )

    department = fields.Selection(availableDepartments, string='Department')

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
    def TreatingButton(self):
        self.state = 'treating'

    def DoneButton(self):
        self.state = 'done'

    def CancelButton(self):
        self.state = 'cancel'

    # Overriding db record create method.
    @api.model
    def create(self, vals):
        vals['state'] = 'sick'
        #if '@' not in vals['email']:
            #raise ValidationError('The Email Address is Incorrect')

        if not self.ValidateEmail(vals['email']):
            raise ValidationError('The Email Address Does not match any users')

        # create(vals) is for the chatter log message.
        # Setting note (description) field to new patient if its empty.
        if not vals.get('note'):
            vals['note'] = "New patient"

        if vals.get('reference', 'New') == 'New':
            vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient') or 'New'

        # vals will be the results entered during record creation.
        # super(ClassStructure, ActualClassWithData)
        return super(HospitalPatient, self).create(vals)
    def ValidateEmail(self, emailString):
        usersList = self.env['res.users'].search([])
        for user in usersList:
            print(user.login)
            if user.login == emailString:
                return True
        return False
