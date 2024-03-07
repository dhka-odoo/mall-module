from odoo import models,fields

class mallShopCategories(models.Model):
    _name = "mall.shop.categories"
    _description = "Mall Shop Categories"

    name = fields.Char('Name',required=True)

    #constraints
    _sql_constraints = [
        ('check_name','unique(name)','A Shop Category name must be unique')
    ]