from odoo import models,fields,api

class AccountMoveInherited(models.Model):
    _inherit="account.move"

    season_id = fields.Many2one("sale.season", required=True)

    # @api.model_create_multi
    # def create(self, vals_list):
    #     for vals in vals_list:
    #         if vals.get('season_id'):
    #             vals['season_id'] = int(vals['season_id'])
    #     moves = super().create(vals_list)
    #     return moves