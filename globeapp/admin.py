from django.contrib import admin
from .models import Location, SMPost, Brand, Language, SMPlatform


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "description")  # Only these two fields exist
    readonly_fields = ("id",)


@admin.register(SMPost)
class SMPostAdmin(admin.ModelAdmin):
    model = SMPost
    readonly_fields = ("id",)


@admin.register(Brand)
class BrandsAdmin(admin.ModelAdmin):
    model = Brand
    readonly_fields = ("id",)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    model = Language
    readonly_fields = ("id",)


@admin.register(SMPlatform)
class SMPlatformAdmin(admin.ModelAdmin):
    model = SMPlatform
    readonly_fields = ("id",)
