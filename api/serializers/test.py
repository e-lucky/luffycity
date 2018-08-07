#!/usr/bin/env python
# -*- coding:utf-8 -*-

from rest_framework import serializers
from api import models

class DemoModelSerializer(serializers.ModelSerializer):

    # 查看所有学位课并打印学位课名称以及授课老师
    teacherName = serializers.CharField(source="teachers__name")
    class Meta:
        model = models.DegreeCourse
        fields = ['name','teacherName']

    # 查看所有学位课并打印学位课名称以及学位课的奖学金
    #     values = serializers.SerializerMethodField()
    #     def get_values(self, obj):
    #         scholarship_list = obj.scholarship_set.all()
    #         return [item.value for item in scholarship_list]
    #     class Meta:
    #         model = models.DegreeCourse
    #         fields = ['name','values']

    # 展示所有的专题课
    # class Meta:
    #     model = models.Course
    #     fields = "__all__"

    # 查看id=1的学位课对应的所有模块名称
    # class Meta:
    #     model = models.Course
    #     fields = ["name"]

    # 获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
    # level_name = serializers.CharField(source="get_level_display")
    # whyStudy = serializers.CharField(source="coursedetail.why_study")
    # whatToStudyBrief = serializers.CharField(source="coursedetail.what_to_study_brief")
    # recommend_courses = serializers.SerializerMethodField()
    # def get_recommend_courses(self,row):
    #     recommend_list = row.coursedetail.recommend_courses.all()
    #     return [ {'id':item.id,'name':item.name} for item in recommend_list]
    # class Meta:
    #     model = models.Course
    #     fields = ["name","level_name","whyStudy","whatToStudyBrief","recommend_courses"]

    # 获取id = 1的专题课，并打印该课程相关的所有常见问题
    # ask = serializers.SerializerMethodField()
    # def get_ask(self,obj):
    #     ask_list = obj.asked_question.all()
    #     return [(item.question,item.answer) for item in ask_list]
    # class Meta:
    #     model = models.Course
    #     fields = ["ask"]

    # 获取id = 1的专题课，并打印该课程相关的课程大纲
    # outline = serializers.SerializerMethodField()
    # def get_outline(self,obj):
    #     outline_list = obj.coursedetail.courseoutline_set.all()
    #     return [(item.title,item.content) for item in outline_list]
    # class Meta:
    #     model = models.Course
    #     fields = ["outline"]

    # 获取id = 1的专题课，并打印该课程相关的所有章节
    # chapter = serializers.CharField(source="coursechapters.name")
    # class Meta:
    #     model = models.Course
    #     fields = ["chapter"]