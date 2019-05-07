# -*- coding: utf-8 -*-

from flectra import api, fields, models
class FacultyInfo(models.Model):
    _name = "faculty.info"

    name = fields.Integer(string="Faculty Id",required=True)
    fac_name = fields.Char(string="Faculty Name")
   # fac_course = fields.Selection([('artificial intelligence', 'Artificial intelligence'),
    #                              ('python', 'Python'),
     #                             ('cloud computing', 'Cloud Computing'),
      #                            ('big data', 'Big Data')], string="Faculty Course")
    start_date = fields.Date(string="calendar")
    student_ids = fields.Many2many("student.info", "student_faculty_rel",
                                    "faculty_id", "student_id", string="Students")
    total_students = fields.Integer(string="Total students", readonly=True)
    faculty_id = fields.Many2one("course.info",required=True,string="Faculty_course")

    @api.multi
    def count_total_students(self):
        print ("IN COUNT students-------", len(self))
        self.total_students = len(self.student_ids)

        count = self.env['student.info'].browse('faculty_ids')
        print("----------------READ---------", count)