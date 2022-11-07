from odoo import api, fields, models


class BooksDeatil(models.Model):
    _name = 'library.books'
    _description = "library books"

    isbn = fields.Char(string="ISBN_no")
    author_id = fields.Many2one('library.author', string="Author", )
    book_reference = fields.Text(string="Book Reference")
    name = fields.Char(string="Name")
    edition_mark = fields.Char(string="Edition Mark")
    date_of_publication = fields.Datetime(string="Date of Publication")
    volume_number = fields.Integer(string="Volume_numbers")
    publication = fields.Char(string="Publication")
    category_id = fields.Many2one('library.category', string="Category")
    img = fields.Binary(string="image")
    status = fields.Boolean(string="Available")

    # student_id = fields.Many2one('library.management',string="Studentname")
    # The author id is connect to one2many moudle author.library
    @api.model
    def create(self, vals):
        # if 'company_id' in vals:
        #     self = self.with_company(vals['company_id'])
        # if vals.get('name', _('New')) == _('New'):
        #     seq_date = None
        #     if 'date_order' in vals:
        #         seq_date = fields.Datetime.context_timestamp(self, fields.Datetime.to_datetime(vals['date_order']))
        #     vals['name'] = self.env['ir.sequence'].next_by_code('sale.order', sequence_date=seq_date) or _('New')
        result = super(BooksDeatil, self).create(vals)
        print("hello",self,vals)
        return result

    def write(self, values):
        print(self)
        result = super(BooksDeatil, self).write(values)
        # print(result)
        return result

    def unlink(self):
        # print(self)
        result = super(BooksDeatil, self).unlink()
        print(result)
        return result

    # def _search(self, args offset=0, limit=None, order=None, count=True, access_rights_uid=None):
    #     result = super(BooksDeatil, self)._search(args=args, offset=offset, limit=limit, order=order, count=count,
    #                                               access_rights_uid=access_rights_uid)
    #     print(self,args,offset,limit,order,count,access_rights_uid,)
    #     return result
