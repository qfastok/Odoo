from odoo import api, fields, models, _, tools


class Partner(models.Model):
    _name = "openacademy.partner"
    _description = "Openacademy Partner"

    name = fields.Char(string='Name')
    instructor = fields.Boolean(string='instructor')
    session_ids = fields.Many2many('openacademy.session', readonly=True, string='Partner')
