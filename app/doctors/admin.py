from django.contrib import admin

from .models import Physician, Schedule

admin.site.register(Physician)
admin.site.register(Schedule)
