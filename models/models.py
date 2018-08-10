# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class edificios(models.Model):
#     _name = 'edificios.edificios'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Edificio(models.Model):
    _name = 'edificios.edificio'

    name = fields.Char(string="Descripción", required=True)
    
    responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsable", index=True)
    
    piso = fields.Integer(string="Número de pisos")
    sub = fields.Integer(string="Número de subsuelos")

class Piso(models.Model):
    _name = 'edificios.piso'

    name = fields.Char(required=True)

    edificio_id = fields.Many2one('edificios.edificio',
        ondelete='cascade', string="Edificio", required=True)