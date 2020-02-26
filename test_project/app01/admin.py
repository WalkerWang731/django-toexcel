# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from . import models

class AdminStudents(admin.ModelAdmin):
    list_display = ('stu_name', 'stu_genders')

    # toexcel_fields declare which data is saved to excel
    toexcel_fields = ('stu_name', 'stu_genders')

    # toexcel_tags declare customize filed name of excel table headers
    toexcel_tags = ('custom_stu_name', 'custom_stu_genders')

    # toexcel_choices_fields and toexcel_choices_dict declare which fields for data conversion,
    # they must exist at the same time
    toexcel_choices_fields = ('stu_genders', )
    toexcel_choices_dict = ('stu_genders_dict',)

admin.site.register(models.Students, AdminStudents)

class AdminStuClass(admin.ModelAdmin):
    list_display = ('class_name', 'all_students',)
    filter_horizontal = ('class_students', )

    # Of course you can also do this, in this example 'all_students' is advanced field, toexcel also supports.
    # And we omitted 'toexcel_tags', so 'toexcel_tags' same to 'toexcel_fields' in default.
    # If not define toexcel_fields in this, toexcel will dump all fields, same to `models.StuClass.object.all().valus()`
    toexcel_fields = list_display

    def all_students(self, obj):
        _l = list()
        for stu_obj in obj.class_students.all():
            _l.append(stu_obj.stu_name)
        return ','.join(_l)

admin.site.register(models.StuClass, AdminStuClass)