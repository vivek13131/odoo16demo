from odoo import api, fields, models


class Library(models.Model):
    _name = 'library.admin'
    _rec_name = "name_id"

    name_id = fields.Many2one('library.management', string="Book Taken list")

