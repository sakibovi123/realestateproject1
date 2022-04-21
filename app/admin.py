from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .resource import AreaResource


# @admin.register("Area")
class AreaImport(ImportExportModelAdmin):
    resource_class =  AreaResource


admin.site.register(Area, AreaImport)


