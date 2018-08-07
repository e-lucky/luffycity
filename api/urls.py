#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.conf.urls import url
from api.views import course, test

urlpatterns = [
    url(r'^courses/', course.CourseViews.as_view()),
    url(r'^demo/', test.DemoView.as_view()),

]
