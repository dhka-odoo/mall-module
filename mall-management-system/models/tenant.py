from odoo import fields,models

class tenant(models.Model):
    _name = "tenant"
    _description = "tenant information"

    name = fields.Char('Tenants name',required=True)
    address = fields.Char('Address')
    tenant_contact = fields.Integer("Contact no.")
    tenant_mobile = fields.Integer("Mobile no.")
    tenant_email = fields.Text('Email',required=True)
    shop_name = fields.Char('Shop Name')
    shop_type = fields.Char('Shop Type')
    shop_num = fields.Integer('Shop No.')
    shop_details = fields.Text('Shop Details')
    company_name = fields.Char('Company Name')
    tenant_type = fields.Selection(
        selection=[('individual','Individual'),('company','company')]
    )
