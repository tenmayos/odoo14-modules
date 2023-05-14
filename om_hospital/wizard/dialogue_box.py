from odoo import api, models, fields


class DialogueBox(models.TransientModel):

    _name = 'dialogue.box.wizard'
    _description = 'Creates a dialogue box with costume messages'

    prompt_msg = fields.Char(string='Message')

    def ConfirmButton(self):
        #TODO: Make the invoice's state posted.
        #TODO: Change the patient's state into billed.
        print('hello')
