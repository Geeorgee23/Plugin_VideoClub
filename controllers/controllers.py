# -*- coding: utf-8 -*-
# from odoo import http


# class PluginVideoclub(http.Controller):
#     @http.route('/plugin_videoclub/plugin_videoclub/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/plugin_videoclub/plugin_videoclub/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('plugin_videoclub.listing', {
#             'root': '/plugin_videoclub/plugin_videoclub',
#             'objects': http.request.env['plugin_videoclub.plugin_videoclub'].search([]),
#         })

#     @http.route('/plugin_videoclub/plugin_videoclub/objects/<model("plugin_videoclub.plugin_videoclub"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('plugin_videoclub.object', {
#             'object': obj
#         })
