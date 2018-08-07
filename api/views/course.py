from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from django.http import HttpResponse
from api.serializers import course
from api.utils import response
from rest_framework.response import Response
from api import models
from rest_framework.pagination import PageNumberPagination  #分页

class CourseViews(APIView):
    def get(self,request,*args,**kwargs):
        ret = response.BaseResponse()
        try:
            queryset = models.Course.objects.all()
            page = PageNumberPagination()
            course_list = page.paginate_queryset(queryset,request,self)
            course_ser = course.CourseModelSerializer(instance=course_list,many=True)
            ret.data = course_ser.data
        except Exception as e:
            ret.code = 500
            ret.error = "获取数据失败"

        return Response(ret.dict)