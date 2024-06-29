
from odoo import models, fields

class Client(models.Model):
    _name = 'realestate.client'
    _description = 'Clientes'

    name = fields.Char(string='Nombre del Cliente', required=True)
    phone = fields.Char(string='Teléfono', required=True)
    email = fields.Char(string='Email')
    address = fields.Char(string='Dirección', required=True)
    cedula = fields.Char(string='Documento de Identidad N°', required=True)
    salario = fields.Float(string='Monto de Salario', required=True)  
    foto_cedula = fields.Binary(string='Foto de Cédula', attachment=True)
    informconf = fields.Binary(string='Informconf', attachment=True)
    liq_salario = fields.Binary(string='Liquidación de Salario', attachment=True)