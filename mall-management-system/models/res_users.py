from odoo import models,fields

class resUsers(models.Model):
    _inherit = "res.users"

    shop_ids = fields.One2many('mall.shop','seller_id',string="Shop Management" )
