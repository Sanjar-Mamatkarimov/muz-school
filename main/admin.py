from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.forms import ModelForm
from . models import SiteSettings, Department, Event, Application, Reward, Teacher, Review, GalleryImage


class SiteSettingsForm(ModelForm):
    class Meta:
        model = SiteSettings
        fields = '__all__'
        widgets = {
            'about_description': CKEditorUploadingWidget(),
        }


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    form = SiteSettingsForm
    list_display = ('logo_text', 'title', 'phone', 'address')
    fieldsets = (
        ('Основные настройки', {
            'fields': ('logo', 'logo_text', 'hero_image', 'title', 'subtitle')
        }),
        ('О школе', {
            'fields': ('about_title', 'about_description', 'about_image')
        }),
        ('Фоновые изображения страниц', {
            'fields': ('contacts_background', 'departments_background', 'events_background', 'gallery_background', 'reviews_background', 'rewards_background', 'teachers_background')
        }),
        ('Контактная информация', {
            'fields': ('address', 'phone', 'instagram_url', 'facebook_url', 'footer_copy', 'map_embed_code')
        }),
    )


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        widgets = {
            'description': CKEditorUploadingWidget(),
        }


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    form = DepartmentForm
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'day', 'month', 'location')
    list_filter = ('month',)
    ordering = ('id',)


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        widgets = {
            'description': CKEditorUploadingWidget(),
        }


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    form = TeacherForm
    list_display = ('full_name', 'specialty', 'experience', 'order')
    list_editable = ('order',)
    search_fields = ('full_name', 'specialty')
    ordering = ('order',)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'instrument', 'age', 'get_application_type_display', 'created_at')
    readonly_fields = ('created_at',)
    list_filter = ('created_at', 'application_type')
    search_fields = ('name', 'phone')
    fields = ('name', 'phone', 'instrument', 'age', 'application_type', 'message', 'created_at')
    
class RewardForm(ModelForm):
    class Meta:
        model = Reward
        fields = '__all__'
        widgets = {
            'description': CKEditorUploadingWidget(),
        }


@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    form = RewardForm
    list_display = ('title', 'order')
    list_editable = ('order',)
    ordering = ('order',)


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    form = ReviewForm
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