from odoo import fields,models

class mallTenant(models.Model):
    _name = "mall.tenant"
    _description = "tenant information"

    name = fields.Char('Tenants name',required=True)
    address = fields.Char('Address')
    tenant_contact = fields.Integer("Contact no.")
    tenant_mobile = fields.Integer("Mobile no.")
    tenant_email = fields.Char('Email')
    shop_name = fields.Char('Shop Name')
    shop_type = fields.Char('Shop Type')
    shop_num = fields.Integer('Shop No.')
    shop_details = fields.Text('Shop Description')
    company_name = fields.Many2one('res.partner',string="Company name",required=True)
    tenant_type = fields.Selection(
        selection=[('individual','Individual'),('company','company')],
        default="individual"
    )
