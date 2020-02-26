# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Students(models.Model):
    class Meta:
        verbose_name_plural = 'StudentsInfo'

    stu_name = models.CharField(max_length=32, null=True, blank=True, verbose_name='name')
    stu_genders_dict = (
        (0, 'girl'),
        (1, 'boy')
    )
    stu_genders = models.IntegerField(choices=stu_genders_dict, null=True, blank=True, verbose_name='genders')

    def __str__(self):
        return self.stu_name


class StuClass(models.Model):
    class Meta:
        verbose_name_plural = 'StudentsOfClass'

    class_name = models.CharField(max_length=32, null=True, blank=True, verbose_name='name')
    class_students = models.ManyToManyField(to=Students, blank=True, verbose_name='students')

    def __str__(self):
        return self.class_name