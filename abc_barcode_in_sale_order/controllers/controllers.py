# -*- coding: utf-8 -*-
# from odoo import http


# class AbcBarcodeInSaleOrder(http.Controller):
#     @http.route('/abc_barcode_in_sale_order/abc_barcode_in_sale_order/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_barcode_in_sale_order/abc_barcode_in_sale_order/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_barcode_in_sale_order.listing', {
#             'root': '/abc_barcode_in_sale_order/abc_barcode_in_sale_order',
#             'objects': http.request.env['abc_barcode_in_sale_order.abc_barcode_in_sale_order'].search([]),
#         })

#     @http.route('/abc_barcode_in_sale_order/abc_barcode_in_sale_order/objects/<model("abc_barcode_in_sale_order.abc_barcode_in_sale_order"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_barcode_in_sale_order.object', {
#             'object': obj
#         })
