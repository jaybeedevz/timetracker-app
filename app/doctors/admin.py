from django.contrib import admin

from .models import Physician, Schedule

class PhysicianAdmin(admin.ModelAdmin):

    list_display = ('id', 'first_name', 'last_name', 'specialization', 'clinic', 'is_active','status')
    list_display_links = ('id', 'first_name', 'last_name')
    list_filter = ('status',)
    list_editable = ('status', 'is_active')
    search_fields = ('first_name', 'last_name', 'specialization')
    list_per_page = 20


class ScheduleAdmin(admin.ModelAdmin):
    list_display =('id', 'physician', 'schedule_day', 'schedule_time_in', 'schedule_time_out')
    list_display_links = ('id', 'physician')
    list_filter = ('physician',)


admin.site.register(Physician, PhysicianAdmin)
admin.site.register(Schedule, ScheduleAdmin)
