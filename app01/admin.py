from django.contrib import admin
from api import models
# Register your models here.

admin.site.register(
    [
        models.CourseCategory,
        models.CourseSubCategory,
        models.DegreeCourse,
        models.Teacher,
        models.Scholarship,
        models.Course,
        models.CourseDetail,
        models.OftenAskedQuestion,
        models.CourseOutline,
        models.CourseChapter,
        models.CourseSection,
        models.Homework,
        models.PricePolicy,
    ]
)