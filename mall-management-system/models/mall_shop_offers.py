from odoo import models,fields,api
from dateutil.relativedelta import relativedelta

class mallShopOffer(models.Model):
    _name = "mall.shop.offer"
    _description = "Mall Shop Offers"

    price = fields.Float("Price")
    status = fields.Selection(
        string = "Status",
        selection=[('accepted','Accepted'),('refused','Refused')],
        copy=False
    )
    partner_id = fields.Many2one('res.partner',string="Partner",required=True)
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
