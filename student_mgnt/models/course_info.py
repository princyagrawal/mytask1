# -*- coding: utf-8 -*-

from flectra import api, fields, models
from flectra.exceptions import ValidationError

class CourseInfo(models.Model):
    _name = "course.info"

    course_code = fields.Integer(string="Course Code no.", required=True)
    name = fields.Char(string = "enter course name")
    course_type = fields.Selection([('ce', 'CE'),
                                   ('ec', 'EC'),
                                   ('civil', 'CIvil'),
                                   ('it', 'IT')], string = "Course type")
    course_credit = fields.Integer(string="Number of Credit")
    course_duration = fields.Float(string="Course Duration Time")
    course_fees = fields.Integer(string="Course Fees")
    start_date = fields.Date(string="calendar")
    student_line = fields.One2many("student.info","course_id",string="Students")

    @api.constrains('course_fees')
    def check_course_fees(self):
        if self.course_fees < 2000 or self.course_fees > 10000:
            raise ValidationError("Course Fees should be between 2000 to 10000.")