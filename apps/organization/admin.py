from django.contrib import admin
from .models import CityDict, CourseOrg

# Register your models here.
@admin.register(CityDict)
class CityDictAdmin(admin.ModelAdmin):
    pass


@admin.register(CourseOrg)
class CourseOrgAdmin(admin.ModelAdmin):
    pass


admin.site.site_header = '也许是意外'
admin.site.name = 'name'
admin.site.site_title = 'title'
admin.site.site_url = 'kk'
admin.site.index_title = '意外'
