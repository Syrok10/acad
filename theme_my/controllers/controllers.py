# -*- coding: utf-8 -*-
from odoo import http

# class ThemeMy(http.Controller):
#     @http.route('/theme_my/theme_my/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/theme_my/theme_my/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('theme_my.listing', {
#             'root': '/theme_my/theme_my',
#             'objects': http.request.env['theme_my.theme_my'].search([]),
#         })

#     @http.route('/theme_my/theme_my/objects/<model("theme_my.theme_my"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('theme_my.object', {
#             'object': obj
#         })