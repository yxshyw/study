from django.contrib import admin
from .models import CityDict, CourseOrg

# Register your models here.
@admin.register(CityDict)
class CityDictAdmin(admin.ModelAdmin):
    pass


@admin.register(CourseOrg)
class CourseOrgAdmin(admin.ModelAdmin):
    pass


admin.site.site_header = 'header'
admin.site.name = 'name'
admin.site.site_title = 'title'
admin.site.site_url = 'url'
admin.site.index_title = 'index_title'
