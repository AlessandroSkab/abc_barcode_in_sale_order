# -*- coding: utf-8 -*-

from odoo import models, fields, api


class abc_barcode_in_sale_order(models.Model):
    _name = 'abc_barcode_in_sale_order.abc_barcode_in_sale_order'
    _description = 'abc_barcode_in_sale_order.abc_barcode_in_sale_order'
    
#Eredito il modulo SaleOrder per accedere alla vista.
class SaleOrder(models.Model):
     _inherit = 'sale.order'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
