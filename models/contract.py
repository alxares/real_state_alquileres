from odoo import models, fields, api

class Contract(models.Model):
    _name = 'realestate.contract'
    _description = 'Real Estate Contract'

    property_id = fields.Many2one('realestate.property', string='Property', required=True)
    client_id = fields.Many2one('realestate.client', string='Client', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date')
    price = fields.Float(string='Price', related='property_id.price')
    
    @api.model
    def create(self, vals):
        # Crear un lead automaticamente en el CRM cuando se crea un contrato
        contract = super(Contract, self).create(vals)
        
        # Crear lead en el CRM
        lead_vals = {
            'name': f"Contract {contract.id}",
            'partner_id': contract.client_id.id,
            'type': 'opportunity',
            'stage_id': self.env.ref('crm.stage_lead1').id,  # Verifica que la referencia sea correcta
            'description': f"Contract for property {contract.property_id.name} with client {contract.client_id.name}",
            'planned_revenue': contract.price,  # Ajusta esto según tus requisitos
        }
        self.env['crm.lead'].create(lead_vals)

        return contract
