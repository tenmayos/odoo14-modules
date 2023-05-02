from odoo import api, fields, models


class CreateAppointmentWizard(models.TransientModel):
    _name = "create.appointment.wizard"
    _description = "This wizard eases appointment creation"

    name = fields.Char(string='Name')

    def ConfirmButton(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/download/patients_age_text?name=%s' % self.name,
            'target': 'self'
        }
