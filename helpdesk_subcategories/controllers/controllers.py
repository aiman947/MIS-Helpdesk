# -*- coding: utf-8 -*-
# from odoo import http


# class HelpdeskSubcategories(http.Controller):
#     @http.route('/helpdesk_subcategories/helpdesk_subcategories', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/helpdesk_subcategories/helpdesk_subcategories/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('helpdesk_subcategories.listing', {
#             'root': '/helpdesk_subcategories/helpdesk_subcategories',
#             'objects': http.request.env['helpdesk_subcategories.helpdesk_subcategories'].search([]),
#         })

#     @http.route('/helpdesk_subcategories/helpdesk_subcategories/objects/<model("helpdesk_subcategories.helpdesk_subcategories"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('helpdesk_subcategories.object', {
#             'object': obj
#         })
