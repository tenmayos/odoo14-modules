# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Hospital Management',
    'version': '1.0',
    'summary': 'He just did nothing wrong',
    'sequence': 10,
    'description': """This is a description""",
    'category': 'Productivity/Productivity',
    'website': 'https://www.yankydanky.com',
    'depends': [
        'mail',
        'sale',
        'report_xlsx'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/patient.xml',
        'views/kids_view.xml',
        'views/sale_inherit.xml',
        'report/patient_card.xml',
        'report/sale_card.xml',
        'report/report.xml',

    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
