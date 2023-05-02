from io import StringIO
from odoo import http
from odoo.http import request
from werkzeug import Response


class HospitalController(http.Controller):
    @http.route('/download/patients_age_text', auth='public')
    def PatientAgesText(self, name):
        patients = request.env['hospital.patient'].search([])

        with StringIO() as textBuffer:
            textBuffer.write('Patient Ages:\n')

            for obj in patients:
                textBuffer.write(str(obj.age) + '\n')

            textBuffer.seek(0)

            response = Response(
                textBuffer.getvalue(),
                headers={
                    'Content-Type': 'application/octet-stream',
                    'Content-Disposition': 'attachment; filename=%s' % name + '.txt'
                }
            )
            return response


