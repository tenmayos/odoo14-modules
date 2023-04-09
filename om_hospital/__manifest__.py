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
        'sale'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/patient.xml',
        'views/sale_inherit.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
