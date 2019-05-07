# -*- coding: utf-8 -*-
import re
from flectra import api, fields, models
from flectra.exceptions import ValidationError

class StudentInfo(models.Model):
    _name = "student.info"


    @api.multi
    def button_done(self):
        for rec in self:
            rec.write({'state': 'done'})

    @api.multi
    def button_reset(self):
        for rec in self:
            rec.write({'state': 'course'})

    @api.multi
    def button_cancel(self):
        for rec in self:
            rec.write({'state': 'cancel'})

    name = fields.Integer(string="Student Roll No.",required=True)
    stu_name = fields.Char(string="Student Name")
    stu_gender = fields.Selection([('male', 'MALE'),
                                   ('female', 'FEMALE')], string="Gender")
    stu_address = fields.Text(string="Student Address")
    stu_mobile = fields.Char(string="Student Mobile Number")
    _sql_constraints = [
        ('name_uniq', 'unique (stu_mobile)', "The mobile number of the student should be unique!")
    ]
    birth_date = fields.Date(string="Student BIrthdate")

    stu_email = fields.Char(string="Student Email",required=True)
    start_date = fields.Date(string="calendar")

    course_id = fields.Many2one("course.info", required=True, string="Course")
    faculty_ids = fields.Many2many("faculty.info", "student_faculty_rel",
                                   "student_id", "faculty_id", string="Faculty")

    state = fields.Selection([
        ('student info', 'Student Info'),
        ('done', 'Done'),
        ('cancel', 'cancel'),
    ], default='student info')

    @api.constrains('stu_mobile')
    def check_stu_mobile(self):
        if len(self.stu_mobile) > 10:
            raise ValidationError("Mobile no should be less than 10 digits")

    @api.onchange('stu_email')
    def validate_mail(self):
        if self.stu_email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.stu_email)
            if match == None:
                raise ValidationError('Not a valid E-mail ID')