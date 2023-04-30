from odoo import http


class HospitalController(http.Controller):
    @http.route('/hello', auth='public')
    def Hello(self, name):
        print("I AM HEEEEEEEEEEEEERE!!" + " " + name)
