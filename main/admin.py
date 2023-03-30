from django.contrib import admin 
from .models import Category, Nike, Image 

class ImagesInline(admin.TabularInline):
    model = Image

@admin.register(Nike)
class NikeAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]
    list_display = ('title','price')



# Register your models here.
admin.site.register(Category)
