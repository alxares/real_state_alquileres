from odoo import models, fields
from datetime import datetime, timedelta

class Property(models.Model):
    _name = 'realestate.property'
    _description = 'Real Estate Property'

    name = fields.Char(string='Título', required=True, default="")
    description = fields.Text(string='Descripción')
    rooms = fields.Integer(string='Habitaciones', default=1, required=True)
    bathrooms = fields.Integer(string='Baños', default=1, required=True)
    parking = fields.Integer(string='Estacionamiento', default=1, required=True)
    address = fields.Char(string='Dirección')
    departamento = fields.Selection([
        ('central', 'Central'),
    ], string='Departamento', default='central')
    city = fields.Selection([
        ('asuncion', 'Asunción'),
        ('aregua', 'Areguá'),
        ('capiata', 'Capiatá'),
        ('fernando_de_la_mora', 'Fernando de la Mora'),
        ('guarambare', 'Guarambaré'),
        ('ita', 'Itá'),
        ('itaugua', 'Itauguá'),
        ('j_augusto_saldivar', 'J. Augusto Saldívar'),
        ('lambare', 'Lambaré'),
        ('limpio', 'Limpio'),
        ('luque', 'Luque'),
        ('mariano_roque_alonso', 'Mariano Roque Alonso'),
        ('nemby', 'Ñemby'),
        ('nueva_italia', 'Nueva Italia'),
        ('san_antonio', 'San Antonio'),
        ('san_lorenzo', 'San Lorenzo'),
        ('villa_elisa', 'Villa Elisa'),
        ('villeta', 'Villeta'),
        ('ypane', 'Ypané'),
    ], string='Ciudad', default='asuncion')
    price = fields.Float(string='Precio')
    property_type = fields.Selection([
        ('casa', 'Casa'),
        ('departamento', 'Departamento'),
        ('duplex', 'Duplex'),
        ('chalet', 'Chalet'),
        ('comercial', 'Comercial'),
    ], string='Tipo de Propiedad', default='casa')
    status = fields.Selection([
        ('disponible', 'Disponible'),
        ('reservado', 'Reservado'),
        ('alquilado', 'Alquilado'),
    ], string='Estado', default='disponible')
    disponibility_date = fields.Datetime(string='Disponible Desde', copy=False, default=lambda self: fields.Datetime.now() + timedelta(days=90))
    # last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    active = fields.Boolean(string="Active", default=True)
#tocar de aca para abajo si todo explota
    image = fields.Binary(string='Fachada de la Propiedad')
    image_ids = fields.Many2many('ir.attachment', string='Fotos de la Propiedad')
    location = fields.Char(string='Ubicación')
    owner_id = fields.Many2one('res.partner', string='Propietario')