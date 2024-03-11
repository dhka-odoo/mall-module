from odoo import models,fields,api
from odoo.exceptions import ValidationError

class mallFloor(models.Model):
    _name = "mall.floor"
    _description = "Mall Floors"

    name = fields.Integer('Floor No.',required=True)
    mall_id = fields.Many2one('malls',string="Mall Name",required=True)
    shop_ids = fields.One2many('mall.shop','floor_num_id',string="Shops")
    shop_count = fields.Integer(compute="_compute_shops")
    number_of_shops = fields.Integer(string='Number of Shops')
    number_of_vacant_shops = fields.Integer(string='Number of Vacant Shops',compute='_compute_vacant_shops')
    occupancy_rate = fields.Float(string='Occupancy Rate', compute='_compute_occupancy_rate')

    #computed fields
    @api.depends('shop_ids')
    def _compute_shops(self):
        for record in self:
            record.shop_count = len(record.shop_ids)

    @api.depends('number_of_vacant_shops','shop_ids','number_of_shops')
    def _compute_vacant_shops(self):
        for record in self:
            if record.shop_ids:
                for shop_record in record.shop_ids:
                    if shop_record.state == 'Offer_Accepted' or shop_record.state == 'On_Rent':
                        record.number_of_vacant_shops = record.number_of_shops - 1
                    else:
                        record.number_of_vacant_shops = record.number_of_shops
            else:
                record.number_of_vacant_shops = record.number_of_shops

    @api.depends('number_of_shops','number_of_vacant_shops')
    def _compute_occupancy_rate(self):
        for record in self:
            if record.number_of_shops:
                record.occupancy_rate = (record.number_of_shops - record.number_of_vacant_shops) / record.number_of_shops * 100
            else:
                record.occupancy_rate = 0.0
    
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"Floor no. {record.name}"

    #pyhton constraints
    @api.constrains('number_of_vacant_shops','number_of_shops')
    def _shop_limits(self):
        for record in self:
            if record.number_of_vacant_shops > record.number_of_shops:
                raise ValidationError(f"Cant put more than {record.number_of_shops} shops on this Floor")
