# __author__ = 'yxshyw'
# __date__ = '2018/7/29 11:24'

from .models import Course, Lesson, Video, CourseResource
import xadmin


class CourseAdmin:
    list_display = ['name', 'desc', 'detail']
    list_filter = ['name', 'desc', 'detail']
    search_fields = ['name', 'desc', 'detail']

class LessonAdmin:
    list_display = ['course', 'name', 'add_time']
    list_filter = ['course__name', 'name']
    search_fields = ['course__name', 'name', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
