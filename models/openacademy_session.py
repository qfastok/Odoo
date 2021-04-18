from odoo import api, fields, models, tools, exceptions


class Session(models.Model):
    _name = "openacademy.session"
    _description = "Openacademy Session"

    name = fields.Char(string='Name', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
    ], default='draft')
    start_date = fields.Date(default=fields.Date.today)
    end_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(string='Float', default=1)
    instructor_id = fields.Many2one('openacademy.partner', string='Instructor id')
    course_ids = fields.Many2one('openacademy.course', ondelete='cascade', required=True)
    attendee_ids = fields.Many2many('openacademy.partner', string='Attendees')
    seats = fields.Integer(string="Number of Seats")
    taken_seats = fields.Float(string='Taken seats', compute='_taken_seats')

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats

    @api.constrains('taken_seats')
    def _check_taken_seats(self):
        for r in self:
            if r.taken_seats > 100:
                raise exceptions.ValidationError("Available seats: %s ,count participants: %s" % (r.seats, r.attendee_ids))

# 	-добавить возможность архивировать сессии, по умолчанию все сессии активные

