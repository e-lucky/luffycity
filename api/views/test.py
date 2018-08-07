#!/usr/bin/env python
# -*- coding:utf-8 -*-

from api import models
from api.serializers import test
from api.utils import response
from rest_framework.views import APIView
from rest_framework.response import Response


class DemoView(APIView):
    """
    作业
    """
    def get(self,request,*args,**kwargs):
        ret = response.BaseResponse()
        try:
            # 查看所有学位课并打印学位课名称以及授课老师
            queryset = models.DegreeCourse.objects.all().values("name","teachers__name")

            # 查看所有学位课并打印学位课名称以及学位课的奖学金
            # queryset = models.DegreeCourse.objects.all()

            # 展示所有的专题课
            # queryset = models.Course.objects.filter(degree_course__isnull=False)

            # 查看id=1的学位课对应的所有模块名称
            # queryset = models.Course.objects.filter(degree_course_id = 1)

            # 获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
            # queryset = models.Course.objects.filter(id=1).first()    # 去掉many=True

            # 获取id = 1的专题课，并打印该课程相关的所有常见问题
            # queryset = models.Course.objects.filter(id=1).first()

            # 获取id = 1的专题课，并打印该课程相关的课程大纲
            # queryset = models.Course.objects.filter(id=1).first()

            # 获取id = 1的专题课，并打印该课程相关的所有章节
            # queryset = models.Course.objects.filter(id=1).first()

            # page = PageNumberPagination()
            # lis = page.paginate_queryset(queryset,request,self)
            obj = test.DemoModelSerializer(instance=queryset,many=True)
            ret.data = obj.data
        except Exception as e:
            ret.code = 500
            ret.error = "获取数据失败"
        return Response(ret.dict)
