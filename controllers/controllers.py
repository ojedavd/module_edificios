# -*- coding: utf-8 -*-
from odoo import http

# class Edificios(http.Controller):
#     @http.route('/edificios/edificios/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/edificios/edificios/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('edificios.listing', {
#             'root': '/edificios/edificios',
#             'objects': http.request.env['edificios.edificios'].search([]),
#         })

#     @http.route('/edificios/edificios/objects/<model("edificios.edificios"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('edificios.object', {
#             'object': obj
#         })