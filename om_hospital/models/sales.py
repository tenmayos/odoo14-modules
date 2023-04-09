from odoo import api, fields, models


class Sales(models.Model):

    _inherit = "sale.order"
    sale_desc = fields.Text(string="Description")
