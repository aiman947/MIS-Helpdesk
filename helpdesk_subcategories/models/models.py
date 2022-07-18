# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HelpdeskTicketTypeExtend(models.Model):
    _inherit = 'helpdesk.ticket'

    # parent_id = fields.Many2one('helpdesk.ticket.type', 'Parent', index=True, ondelete='cascade')
    # parent_path = fields.Char(index=True)
    # child_id = fields.One2many('helpdesk.ticket.type', 'parent_id', 'Child')
    subtype_id = fields.Many2one('helpdesk.ticket.subtype',string='Subtype', domain=[('type_id', '=', 'ticket_type_id')], ondelete='cascade')
    item_id = fields.Many2one('helpdesk.ticket.item',string='Item', domain=lambda self: [('subtype_id', '=', self.subtype_id.id)], ondelete='cascade')

    @api.onchange('ticket_type_id')
    def _onchange_ticket_type_id(self):
        return {'domain': {'subtype_id': [('type_id', '=', self.ticket_type_id.id)]}}

    @api.onchange('subtype_id')
    def _onchange_subtype_id(self):
        return {'domain': {'item_id': [('subtype_id', '=', self.subtype_id.id)]}}

class HelpdeskSubtype(models.Model):
    _name = 'helpdesk.ticket.subtype'
    _description = '  '

    sequence = fields.Integer(default=10)
    name = fields.Char('name', required=True)
    type_id = fields.Many2one('helpdesk.ticket.type',string='Ticket Type', required=True)


class HelpdeskSubitem(models.Model):
    _name = 'helpdesk.ticket.item'
    _description = ''
    
    sequence = fields.Integer(default=10)
    name = fields.Char('name', required=True)
    subtype_id = fields.Many2one('helpdesk.ticket.subtype',string='Subtype', required=True)
