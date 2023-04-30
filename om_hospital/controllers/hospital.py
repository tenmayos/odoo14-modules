from io import StringIO
from odoo import http
from odoo.http import request
from werkzeug import Response


class HospitalController(http.Controller):
    @http.route('/hello', auth='public')
    def Hello(self, name):
        patients = request.env['hospital.patient'].search([])
        for obj in patients:
            print(obj.age)

        with StringIO() as textBuffer:
            for obj in patients:
                textBuffer.write(str(obj.age) + '\n')

            textBuffer.seek(0)

            response = Response(
                textBuffer.getvalue(),
                headers={
                    'Content-Type': 'application/octet-stream',
                    'Content-Disposition': 'attachment; filename=%s' % name + '.txt',
                },
            )
            return response


