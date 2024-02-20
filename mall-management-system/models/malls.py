from odoo import fields,models,api

class malls(models.Model):
    _name = "malls"
    _description = "mall management"
    _inherit = ["mail.thread","mail.activity.mixin"]

    name = fields.Char('Mall/Complex name',required=True,tracking=True)
    address = fields.Char('Address',tracking=True)
    owner = fields.Char('Owner',tracking=True)
    owner_contact = fields.Integer("Owner's Contact no.",tracking=True)
    owner_email = fields.Char('Email',tracking=True)
    shop_ids = fields.One2many('mall.shop','mall_name_id', string="Shops",tracking=True)
    description = fields.Text('Mall Description')
    mall_area = fields.Float('Mall Area (sqm)')
    floors = fields.Integer('No. of Floors',default=1)
    num_shops = fields.Integer('No. of Shops',compute="_compute_num_shops")
    parking = fields.Boolean('Parking')
    num_parking_celler = fields.Integer('No. of Parking Cellers')
    parking_area = fields.Float('Parking Area')

    @api.onchange("parking")
    def _onchange_garden(self):
        if self.parking == True:
            self.num_parking_celler = 1
            self.parking_area = 10
        else:
            self.num_parking_celler = None
            self.parking_area = None

    @api.depends('shop_ids')
    def _compute_num_shops(self):
        for record in self:
            record.num_shops = len(record.shop_ids)
