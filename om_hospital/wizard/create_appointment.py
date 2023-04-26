from odoo import api, fields, models


class CreateAppointmentWizard(models.TransientModel):
    _name = "create.appointment.wizard"
    _description = "This wizard eases appointment creation"

    name = fields.Char(string='Name')
