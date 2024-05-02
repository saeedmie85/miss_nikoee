from django.contrib import admin
from .models import Post, Category
# Register your models here.
# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','jalali_publish','jalali_created','jalali_updated','status',
                    'category']
    list_filter=['publish','status','author']
    search_fields=['title','body']
    prepopulated_fields = {'slug':['title']}
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =['title','slug','description','status','position','thumbnail']
    prepopulated_fields = {'slug':['title']}