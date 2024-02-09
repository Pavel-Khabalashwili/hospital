from django.utils.html import format_html
from django.contrib import admin
from .models import Applications


@admin.register(Applications)
class ApplicationsAdmin(admin.ModelAdmin):
    list_display = "title", "desk", "status", "show_photo",
    list_display_links = "title", "desk", "status", "show_photo",
    ordering = "pk",
    readonly_fields = ("show_photo",)
    search_fields = "title", "desk",
    
    exclude = ("status",)  # Скрыть поле "status" в панели редактирования записи

    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
    
   
    
    def show_photo(self, obj : Applications) -> str:
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        else:
            return ''
    show_photo.short_description = 'Изображение'
