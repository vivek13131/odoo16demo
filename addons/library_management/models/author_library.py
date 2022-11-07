from odoo import api, fields, models


class author(models.Model):
    _name = 'library.author'
    _description = 'author library'

    name = fields.Char(string="Authorname")
    date_of_birth = fields.Date(string="DOB")
    awards = fields.Text(string="Awards")
    biography = fields.Text(string="Biography")
    image = fields.Binary(string="Image")
    Books_ids = fields.Many2many('library.books', 'author_book_rel', 'author_id' 'book_id', string="Books")
    book_log_ids = fields.One2many('library.books','author_id',string="Book log")


