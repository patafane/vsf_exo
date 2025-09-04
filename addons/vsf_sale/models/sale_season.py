from odoo import models,fields,api


class SaleSeason(models.Model):
    _name="sale.season"
    _description="season"

    name = fields.Char(required=True)
    sequence = fields.Integer()