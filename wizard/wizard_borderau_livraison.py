# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError
class wizard_stock_bordereau_livraison(models.TransientModel):
    _name = 'wizard.stock.bordereau.livraison'
    _description ='Borderau de livraisons des articles'


    date_start = fields.Datetime('Date de debut', index=True, required=True)
    date_end = fields.Datetime('Date de fin', index=True, required=True)
    company_ids = fields.Many2many('res.company', string="Compagnies")


    def print_bordereau(self):
        datas = {
            'date_start': self.date_start,
            'date_end': self.date_end,
            'company_ids':self.company_ids.ids
        }
        return self.env.ref('stock.action_report_bordereau').report_action(self, data=datas)




        