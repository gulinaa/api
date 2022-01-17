from django.contrib import admin
from .models import Hotel, HotelImage, Comment, Category

admin.site.register(Comment)
admin.site.register(Category)

class HotelImageInLine(admin.TabularInline):
    model = HotelImage
    max_num = 50
    min_num = 1


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    inlines = [HotelImageInLine, ]

