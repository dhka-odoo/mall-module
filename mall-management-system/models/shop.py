from odoo import fields,models

class shop(models.Model):
    _name = "mall.shop"
    _description = "shop in the mall"

    name = fields.Char('Shop name',required=True)
    shop_num = fields.Integer('Shop no.')
    tenant = fields.Char('Tenant')
    floor_num = fields.Integer('Floor no.')
    shop_area = fields.Float('Shop Area (sqm)')
    shop_rent = fields.Float('Shop Rent')
    
    