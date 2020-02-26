#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# file:urls.py
# author: https://github.com/WalkerWang731

from django.conf.urls import url
from toexcel import views

urlpatterns = [
    url(r'^dump', views.dump),
]
