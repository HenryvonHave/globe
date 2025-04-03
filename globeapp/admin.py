from django.contrib import admin
from .models import Location, SMPost


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "description")  # Only these two fields exist


@admin.register(SMPost)
class SMPostAdmin(admin.ModelAdmin):
    model = SMPost
