from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

@admin.register(SchoolSettings)
class SchoolSettingsAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'motto', 'created_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('school_name', 'logo', 'motto', 'aim', 'history')
        }),
        ('Contact Information', {
            'fields': ('address', 'phone', 'email', 'google_map_embed')
        }),
        ('Design Settings', {
            'fields': (
                'navbar_color', 'navbar_font_color',
                'footer_color', 'footer_font_color',
                'body_font'
            )
        }),
    )

@admin.register(HeroImage)
class HeroImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'transition_style', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    list_filter = ('is_active', 'transition_style')
    search_fields = ('title', 'caption')

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'section_type', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    list_filter = ('section_type', 'is_active')
    search_fields = ('title', 'content')

@admin.register(SubSection)
class SubSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    list_filter = ('section__section_type', 'is_active')
    search_fields = ('title', 'content')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active', 'date')
    search_fields = ('title', 'description', 'location')

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_achieved', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('title', 'description')
    date_hierarchy = 'date_achieved'

@admin.register(SchoolCalendar)
class SchoolCalendarAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('title', 'year')

@admin.register(FeeStructure)
class FeeStructureAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_editable = ('is_active',)
    search_fields = ('title', 'description')

@admin.register(NavbarAdvert)
class NavbarAdvertAdmin(admin.ModelAdmin):
    list_display = ('text', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    search_fields = ('text',)


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    search_fields = ('name', 'description')
    list_filter = ('is_active',)


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'image_preview', 'is_active', 'order', 'created_at')
    list_editable = ('is_active', 'order')
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'description')
    readonly_fields = ('image_preview',)

    fieldsets = (
        (None, {
            'fields': ('title', 'category', 'image', 'image_preview', 'description')
        }),
        ('Settings', {
            'fields': ('is_active', 'order')
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 50px; max-width: 100px;" />')
        return "No Image"

    image_preview.short_description = 'Preview'