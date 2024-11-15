from django.contrib import admin
from news_app.models import CategoryNews, New

# Register your models here.


@admin.register(CategoryNews)
class CategoryAdminModel(admin.ModelAdmin):
    search_field = ["category_name"]
    list_filter = ["created_at"]


@admin.register(New)
class NewAdminModel(admin.ModelAdmin):
    search_fields = ["new_name"]
    list_filter = ["created_at"]