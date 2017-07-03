# -*- coding: utf-8 -*-
{
    'name'     : 'InfoSaône - Module Odoo Grain de Sel',
    'version'  : '0.1',
    'author'   : 'InfoSaône',
    'category' : 'InfoSaône/iCom',


    'description': """
InfoSaône - Module Odoo Grain de Sel
===================================================
""",
    'maintainer' : 'InfoSaône',
    'website'    : 'http://www.infosaone.com',
    'depends'    : [
        'base',
        'stock',
        'sale',
        'point_of_sale',
        'pos_restaurant',
        'mail',
        'account',
        'account_accountant',
        'purchase',
        'board',
        'calendar',
],
    'data' : [
        'views/point_of_sale.xml',
        'views/pos_order_view.xml',
    ],
    'installable': True,
    'application': True,
    'qweb': ['static/src/xml/pos.xml'],
}