from odoo import api, models, fields


class DialogueBox(models.TransientModel):

    _name = 'dialogue.box.wizard'
    _description = 'Creates a dialogue box with costume messages'

    prompt_msg = fields.Char(string='Message')
    inv_id = fields.Integer()

    def ConfirmButton(self):
        #TODO: Make the invoice's state posted.
        inv = self.env['account.move'].search([('id', '=', self.inv_id)])
        inv.state = 'posted'

        #TODO: Change the patient's state into billed.
        patient_record = self.env['hospital.patient'].search([('associated_invoice_id', '=', self.inv_id)])
        patient_record.state = 'sick'

