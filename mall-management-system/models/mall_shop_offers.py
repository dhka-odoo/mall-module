from odoo import models,fields,api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError

class mallShopOffer(models.Model):
    _name = "mall.shop.offer"
    _description = "Mall Shop Offers"
    _order = "price desc"

    price = fields.Float("Price")
    status = fields.Selection(
        string = "Status",
        selection=[('accepted','Accepted'),('refused','Refused')],
        copy=False
    )
    partner = fields.Many2one('mall.tenant',string="Partner",required=True)
    shop_id= fields.Many2one('mall.shop',string="Shop",required=True)
    validity = fields.Integer('Validity(days)',default=7)
    date_deadline = fields.Date('Deadline',compute="_compute_deadline",inverse="_inverse_deadline")

    @api.depends("validity","date_deadline","create_date")
    def _compute_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + relativedelta(days=record.validity)
            else:
                record.date_deadline = fields.Date.today() + relativedelta(days=record.validity)

    def _inverse_deadline(self):
        for record in self:
            record.validity = record.date_deadline.day - record.create_date.day

    def offer_accept(self):
        for record in self:
            if record.shop_id.shop_rent == 0:
                record.status = "accepted"
                record.shop_id.tenant_id = record.partner
                record.shop_id.shop_rent = record.price
                # record.shop_id.name = record.partner.shop_name    
                record.shop_id.state = "Offer_Accepted"
            else:
                raise UserError("Only one offer can be accepted for a given shop!")
    def offer_refuse(self):
        for record in self:
            if record.status == "accepted":
                record.status = "refused"
                record.shop_id.tenant_id = ""
                record.shop_id.shop_rent = 0
            else:
                record.status = "refused"

    @api.model
    def create(self,vals):
        shop = self.env['mall.shop'].browse(vals['shop_id'])
        shop.state = "Offer_Received"
        if shop.best_price >= vals["price"]:
            raise UserError("The offer must be higher than %.2f" % shop.best_price)
        return super().create(vals)
