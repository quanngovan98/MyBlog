from django.contrib import admin
from .models import Post
from .models import Category


class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'category', 'date']
	list_filter = ['date']
	search_fields = ['title']
	

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
