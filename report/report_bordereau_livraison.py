# -*- coding:Utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError
class bordereau_livraison_report_parser(models.AbstractModel):
    _name = 'report.stock.report_picking_bordereau'
    _description = 'Rapport  de livraisons des articles'


    def _get_report_values(self, docids, data=None):
        domain = [('state', '=', 'done')]
        if data.get('date_start'):
            domain.append(('date_done', '>=', data.get('date_start')))
        if data.get('date_end'):
            domain.append(('date_done', '<=', data.get('date_end')))
        if data.get('company_ids'):
            domain.append(('id', 'in', data.get('company_ids')))
        
        docs = self.env['stock.picking'].search(domain)
        
        company_ids = self.env['stock.picking'].browse(data.get('company_ids'))
        
        data.update({'company_ids': ",".join([company.name for company in company_ids])})

        article_ids = list(set(docs.mapped("move_ids_without_package.name")))

        quantity_ids =[]
        
        #Quantite d'article par article
        for article in article_ids:
            quantity = 0
            for doc in  docs :
                if doc.move_ids_without_package[0].name == article:
                    quantity = quantity + doc.move_ids_without_package[0].product_uom_qty
            quantity_ids.append(quantity)

        #raise UserError(_(len(article_ids)))
                
        return {
            'doc_ids': docs.ids,
            'doc_model': 'stock.picking',
            'docs': docs,
            'datas': data,
            'article_ids': article_ids,
            'quantity_ids':quantity_ids
            
        }

    