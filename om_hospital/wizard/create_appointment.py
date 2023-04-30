import base64
from io import StringIO
from werkzeug.wrappers import Response
from odoo import api, fields, models



class CreateAppointmentWizard(models.TransientModel):
    _name = "create.appointment.wizard"
    _description = "This wizard eases appointment creation"

    name = fields.Char(string='Name')

    def ConfirmButton(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/hello?name=%s' % self.name,
            'target': 'self'
        }
        # patients = self.env['hospital.patient'].search([])
        # print(self.name)
        # with StringIO() as textBuffer:
        # for obj in patients:
        #   textBuffer.write(str(obj.age) + '\n')

        # textBuffer.seek(0)

        # with open('patients.txt', 'w') as file:
        #   file.write(textBuffer.getvalue())

        # TODO: create a controller to handle the download
