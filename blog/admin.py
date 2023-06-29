from django.contrib import admin
from .models import New, Image
# Register your models here.


class ImageInline(admin.TabularInline):
    model = Image

class NewAdmin(admin.ModelAdmin):
    list_display = ['tittle', 'description', 'created_at']
    list_filter = ['tittle']
    search_fields = ['tittle']
    inlines = [ImageInline]

admin.site.register(New, NewAdmin)
admin.site.register(Image)
