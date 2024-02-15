from odoo import fields,models

class malls(models.Model):
    _name = "malls"
    _description = "mall management"
    _inherit = ["mail.thread","mail.activity.mixin"]

    name = fields.Char('Mall/Complex name',required=True,tracking=True)
    address = fields.Char('Address',tracking=True)
    owner = fields.Char('Owner',required=True,tracking=True)
    owner_contact = fields.Integer("Owner's Contact no.",tracking=True)
    owner_email = fields.Char('Email',required=True,tracking=True)
    shop_ids = fields.One2many('mall.shop','mall_name_id', string="Shops")
