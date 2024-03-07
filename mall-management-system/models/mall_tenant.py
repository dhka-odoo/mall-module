from odoo import fields,models

class mallTenant(models.Model):
    _name = "mall.tenant"
    _description = "tenant information"

    name = fields.Char('Tenants name',required=True)
    address = fields.Char('Address')
    tenant_contact = fields.Integer("Contact no.")
    tenant_mobile = fields.Integer("Mobile no.")
    tenant_email = fields.Char('Email')
    shop_num = fields.One2many('mall.shop','tenant_id')
    company_name = fields.Many2one('res.partner',string="Company name",required=True)
    tenant_type = fields.Selection(
        selection=[('individual','Individual'),('company','company')],
        default="individual"
    )
