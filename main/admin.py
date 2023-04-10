from django.contrib import admin 
from .models import Category, Nike, Image, Order, OrderItem 

class ImagesInline(admin.TabularInline):
    model = Image

@admin.register(Nike)
class NikeAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]
    list_display = ('title','price')



# Register your models here.
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
