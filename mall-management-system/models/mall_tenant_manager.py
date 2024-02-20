from odoo import fields,models

class mallTenantManager(models.Model):
    _name = "mall.tenant.manager"
    _description = "tenant manager information"

    name = fields.Char('Tenants name',required=True)
    address = fields.Char('Address')
    tenant_manager_contact = fields.Integer("Contact no.")
    tenant_manager_mobile = fields.Integer("Mobile no.")
    tenant_manager_email = fields.Char('Email')
    tenant_assigned_ids = fields.One2many('mall.tenant','tenant_manager_id')
