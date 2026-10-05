from django.contrib import admin

from .models import ContactMessage, JourneyEntry


@admin.register(JourneyEntry)
class JourneyEntryAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "published")
    list_filter = ("published",)
    search_fields = ("title", "summary", "body")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "date"


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created", "handled")
    list_filter = ("handled",)
    readonly_fields = ("name", "email", "message", "created")
