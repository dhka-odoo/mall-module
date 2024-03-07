from odoo import fields,models,api
from odoo.exceptions import UserError

class shop(models.Model):
    _name = "mall.shop"
    _description = "shop in the mall"
    _inherit = ["mail.thread","mail.activity.mixin"]

    name = fields.Char('Shop name')
    shop_num = fields.Integer('Shop no.',required=True)
    tenant_id = fields.Many2one('mall.tenant',string="Tenant")
    description = fields.Text('Description')
    floor_num = fields.Integer('Floor no.',default=1)
    shop_area = fields.Float('Shop Area (sqm)')
    shop_rent = fields.Float('Shop Rent')
    mall_name_id = fields.Many2one('malls',string="Mall name",required=True)
    best_price = fields.Float('Best Offer',compute="_compute_best_price")
    state = fields.Selection(
        string='Status',
        selection=[('New','New'),('Offer_Received','Offer Received'),('Offer_Accepted','Offer Accepted'),('On_Rent','On Rent'),('Canceled','Canceled')],
        default='New'
    )
    offer_ids = fields.One2many("mall.shop.offer","shop_id", string="Offers")
    seller_id = fields.Many2one('res.users',string="Salesman",default=lambda self: self.env.user,tracking=True)
    category_id = fields.Many2one('mall.shop.categories', string="Shop Catagory")
    date_on_rent = fields.Date('Starting Date')

    @api.depends("offer_ids")
    def _compute_best_price(self):
        for record in self:
            if record.offer_ids:
                record.best_price = max(record.offer_ids.mapped("price"))
            else:
                record.best_price = 0

    def on_rent_action(self):
        for record in self:
            if record.state != "Canceled":
                record.state = "On_Rent"
                record.date_on_rent = fields.Date.today()
            else:
                raise UserError("A Canceled property cannot be given on rent") 
        return True
    
    def cancel_action(self):
        for record in self:
            if record.state != "On_Rent":
                record.state = "Canceled"
            else:
                raise UserError("A property given on rent cannot be Canceled")     
        return True

    @api.ondelete(at_uninstall=False)
    def _prevent_deletion_shop(self):
        for record in self:
            if record.state != "New" and record.state != "Canceled":
                raise UserError("Only New and Canceled Shops can be deleted")
