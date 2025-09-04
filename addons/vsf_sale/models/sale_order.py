from odoo import models,fields,api

class SaleOrderInherited(models.Model):
    _inherit="sale.order"

    season_id=fields.Many2one("sale.season",string="Saison" ,required=True ,)

    def _prepare_invoice(self):
        vals = super()._prepare_invoice()
        if self.season_id:
            vals['season_id'] = self.season_id.id
        return vals