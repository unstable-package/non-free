from django.contrib import admin
from main import models


class CompanyInfoAdmin(admin.ModelAdmin):
    pass


class JobInfoAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.JobInfo, JobInfoAdmin)
admin.site.register(models.CompanyInfo, CompanyInfoAdmin)
