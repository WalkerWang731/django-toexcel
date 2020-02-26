# Django-toexcel

## Introduction

Django-toexcel is a simple Django app used to dump excel files from django models. It‘s for users who are already skilled with Django-admin. Django-toexcel than djano-import-export support more version and  more simple. But same to name, Django-toexcel not support import.

## Features

* Simple use and just 3 steps for your Django project to provide dump excel files
* Support all Django versions. include 1.x, 2.x, 3.x
* Do not generate files in server, dump excel files by JavaScript in user browser
* Auth and permission management base on Django-admin

## Quick start

1.Copy "toexcel" to your django project like "./test\_project"

2.Add "toexcel" to your INSTALLED\_APPS setting like this:

```
    INSTALLED_APPS = [
        ...
        'toexcel',
    ]
```

3.Include the toexcel URL conf in your project urls.py like this:

```
from django.conf.urls import url, include
from django.contrib import admin
import toexcel.urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^toexcel/', include(toexcel.urls))
]
```
4.Start the development server like this:

```
python manage.py runserver 127.0.0.1:8000
```

5.Request in browser \(you'll need the Admin app enabled\) like this:

```
http://127.0.0.1:8000/toexcel/dump?app=app01&admin=AdminStudents&models=Students
```

## Project example

./test\_project is Django project. You can start this project and enjoy Django-toexcel

Defult user and password:

> admin
>
> qwert123456

## Advanced

Advanced function should in your Django app's admin.py like ./test\_django/app01/admin.py

Use of Django-toexcel built-in property advanced features

### toexcel\_fields

_toexcel\_fields_ declare which data is saved to excel. If not declare this, then default this models class all fields.

### toexcel\_tags

_toexcel\_tags_ declare customize filed name of excel table headers. If not declare this, then default use the every fields object's _verbose\_name_ property

> If your use _toexce\_fields_ and _toexce\_tags_ ,  they must be one by one

### toexcel\_choices\_fields / toexcel\_choices\_dict

_toexcel\_choices\_fields_ and _toexcel\_choices\_dict_ declare which fields for data conversion when the fields property include choices. They must be one by one and exist at the same time.

## About virtual fields or function fields

Django-toexcel support virtual fields or function fields, like advanced examle: admin.AdminStuClass.all\_students

## Advanced example

```
# models.py
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
```

    # admin.py
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

## Request URL

> URL: /toexcel/dump

> Method: GET

### Parameters

| **Name** | **Explain** |
| :--- | :--- |
| app | your app name \(directory name\) |
| models | your class name in models.py |
| admin  | your register class in admin.py |

### Request example

```
http://127.0.0.1:8000/toexcel/dump?app=app01&admin=AdminStudents&models=Students
```

## Suggest

Because use to django's render method, we suggest no more than 50,000 data.

If more than 50,000 data, then you should modify the source code,and replace django's render method to ajax, maybe more data can be supported

