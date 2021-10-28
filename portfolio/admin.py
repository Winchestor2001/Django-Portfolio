from django.contrib import admin
from . import models



@admin.register(models.MyInfoConfig)
class MyInfoConfig_admin(admin.ModelAdmin):
    list_display = ['myName', 'mySurname', 'my_location_link']


@admin.register(models.Portfolio)
class Portfolio_admin(admin.ModelAdmin):
    list_display = ['category', 'project_date', 'project_url']




admin.site.register(models.AboutInfoConfig)
admin.site.register(models.FactsInfoConfig)
admin.site.register(models.SkillsInfoConfig)





