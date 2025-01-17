from odoo import models, fields

class RealEstateTenant(models.Model):
    _inherit = 'res.partner'

    is_tenant = fields.Boolean(string='Is Tenant', default=False)
    # rental_contract_ids = fields.OneToMany('real.estate.contract', 'client_id', string='Rental Contracts')
    # rented_property_ids = fields.One2many('sale.order', 'tenant_id', string='Rented Properties')
