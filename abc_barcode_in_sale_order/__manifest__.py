# -*- coding: utf-8 -*-
{
    'name': "abc_barcode_in_sale_order",

    'summary': """
        Modulo che permette di inserire il Barcode relativo all'id 
        dell'Ordine di Vendita nel pdf dello stesso Ordine di Vendita.""",

    'description': """
        Modulo che permette di inserire il Barcode relativo all'id 
        dell'Ordine di Vendita nel pdf dello stesso Ordine di Vendita.
    """,

    'author': "A.B.C. srl",
    'website': "https://www.abcstrategie.it/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'report/reportWithBarcode.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
