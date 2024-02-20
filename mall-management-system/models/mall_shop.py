from odoo import fields,models,api
from odoo.exceptions import UserError

class shop(models.Model):
    _name = "mall.shop"
    _description = "shop in the mall"

    name = fields.Char('Shop name',required=True)
    shop_num = fields.Integer('Shop no.')
    tenant_id = fields.Many2one('mall.tenant',string="Tenant")
    description = fields.Text('Description')
    floor_num = fields.Integer('Floor no.')
    shop_area = fields.Float('Shop Area (sqm)')
    shop_rent = fields.Float('Shop Rent')
    mall_name_id = fields.Many2one('malls',string="Mall name")
    state = fields.Selection(
        string='Status',
        selection=[('New','New'),('Offer_Received','Offer Received'),('Offer_Accepted','Offer Accepted'),('On_Rent','On Rent'),('Canceled','Canceled')],
        default='New'
    )
    offer_ids = fields.One2many("mall.shop.offer","shop_id", string="Offers")

    def on_rent_action(self):
        for record in self:
            if record.state != "Canceled":
                record.state = "On_Rent"
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
