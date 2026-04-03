from django.contrib import admin
from . models import SiteSettings, Department, Event, Application, Reward, Teacher, Review, GalleryImage


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('logo_text', 'title', 'phone', 'address')
    fieldsets = (
        ('Основные настройки', {
            'fields': ('logo', 'logo_text', 'hero_image', 'title', 'subtitle')
        }),
        ('О школе', {
            'fields': ('about_title', 'about_description', 'about_image')
        }),
        ('Контактная информация', {
            'fields': ('address', 'phone', 'instagram_url', 'facebook_url', 'footer_copy')
        }),
    )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'day', 'month', 'location')
    list_filter = ('month',)
    ordering = ('id',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'specialty', 'experience', 'order')
    list_editable = ('order',)
    search_fields = ('full_name', 'specialty')
    ordering = ('order',)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'instrument', 'age', 'created_at')
    readonly_fields = ('created_at',)
    list_filter = ('created_at',)
    search_fields = ('name', 'phone')
    fields = ('name', 'phone', 'instrument', 'age', 'message', 'created_at')
    
@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    ordering = ('order',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'created_at', 'is_published')
    list_filter = ('rating', 'is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('name', 'text')
    readonly_fields = ('created_at',)


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'created_at', 'is_published')
    list_filter = ('is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('title', 'caption', 'event_date')
    readonly_fields = ('created_at',)