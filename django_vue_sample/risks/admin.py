from django.contrib import admin

from . import models


admin.site.register(models.RiskType)
admin.site.register(models.CustomField)
admin.site.register(models.CustomFieldOption)
