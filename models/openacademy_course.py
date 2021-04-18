from odoo import api, fields, models, _, tools


class Course(models.Model):
    _name = "openacademy.course"
    _description = "Openacademy Course"

    name = fields.Char(string='Name', required=True)
    description = fields.Text('Description')
    responsible_id = fields.Many2one('openacademy.partner', string='Course')
    session_ids = fields.One2many('openacademy.session', 'course_ids', string="Sessions")
    level = fields.Selection([
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ])
