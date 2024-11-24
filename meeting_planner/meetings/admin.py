from django.contrib import admin
from django.contrib.admin import ModelAdmin

from meetings.models import Meeting, Room

# Register your models here.

admin.site.register(Room)

@admin.register(Meeting)
class MeetingAdmin(ModelAdmin):
    list_display = ("id", "title", "date", "start_time", "room")
    ordering = ("date", "start_time")
    search_fields = ("title",)
