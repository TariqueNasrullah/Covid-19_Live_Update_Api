from django.contrib import admin
from . import models

admin.site.register(models.CoronaData)
admin.site.register(models.CountryData)
