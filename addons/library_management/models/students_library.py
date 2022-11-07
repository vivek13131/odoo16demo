from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
from datetime import datetime, date, timedelta


class StudentsDetails(models.Model):
    _name = 'library.management'
    _description = "library Students"

    roll_no = fields.Integer(string='Roll Number')
    name = fields.Char(string='Name')
    address = fields.Text(string='Address')
    mobile_no = fields.Char(string='Mobile Number')
    course = fields.Selection([
        ('information technology', 'INFOMATION TECHNOLOGY'),
        ('computer Engineering', 'COMPUTER ENGINEERING'),
    ], string=' Course ')
    product_id = fields.Many2many('library.books', string="product")
    date_of_birth = fields.Date(string="Dob",)

    # book info page
    book_taken = fields.Datetime(string="BOOK TAKEN DATE")
    book_return = fields.Datetime(string="BOOK RETURN DATE")
    fee = fields.Integer(string="FEE for Late ")

    @api.model
    def create(self, vals):
        dob = [vals]
        dates = vals['date_of_birth']
        # print(datetime.today().date())
        if vals['date_of_birth']:
            if str(dates) >= str(datetime.today().date()):
                raise ValidationError(_('DOB should be less then Today\'s Date.'))
        if not vals['date_of_birth']:
            raise ValidationError(_("please enter your date birth"))
        if 'date_of_birth' not in dob:
            print("The DOB is is exit")
        else:
            print("The Dob is not exit")
        result = super(StudentsDetails, self).create(vals)
        # print(datetime.today())
        return result

    def write(self, vals):
        dob = [vals]
        dates = vals['date_of_birth']
        # print(datetime.today().date())
        if vals['date_of_birth']:
            if str(dates) >= str(datetime.today().date()):
                raise ValidationError(_('DOB should be less then Today\'s Date.'))
        if not vals['date_of_birth']:
            raise ValidationError(_("please enter your date birth"))
        if 'date_of_birth' in dob:
            print("The DOB is is exit")
        else:
            print("The Dob is not exit")
        result = super(StudentsDetails, self).write(vals)
        return result
