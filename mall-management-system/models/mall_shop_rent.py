from odoo import fields,models,api
from dateutil.relativedelta import relativedelta

class mallShopRent(models.Model):
    _name="mall.shop.rent"
    _description="Shop Rent Generator"

    name = fields.Char(string='Rent id', required=True,readonly=True, default=lambda self: ('New'))
    shop_id = fields.Many2one('mall.shop')
    shop_name = fields.Char('Shop Name',related="shop_id.name")
    mall_name_id = fields.Many2one('malls',related="shop_id.mall_name_id")
    tenant_id = fields.Many2one('mall.tenant',related="shop_id.tenant_id")
    rent = fields.Float('Rent',related="shop_id.shop_rent")
    start_date = fields.Date('Start Date',required=True)
    end_date = fields.Date('End Date',required=True)
    duration = fields.Selection([
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('annually', 'Annually')
    ], string='Duration', required=True, default='monthly')
    state = fields.Selection(
        string='Status',
        selection=[('Draft','Draft'),('Rent_Received','Rent Received')],
        default='Draft'
    )
    due_date = fields.Date('Due Date',copy=False,default=fields.Date.today()+relativedelta(days=7))

    def rent_received_action(self):
        for record in self:
            record.state = "Rent_Received"
        return True

    @api.model
    def create(self,vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('mall.shop.rent')
        return super(mallShopRent,self).create(vals)
