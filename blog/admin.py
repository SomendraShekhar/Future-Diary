from django.contrib import admin
from .models import Category, Post, Comment
from django.contrib.auth.models import User

# Register your models here.

# for configuration of Category admin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'description', 'url', 'add_date')
    search_fields = ('title',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('commentedPost','name','comm')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'cat', 'image', 'user', 'get_likes')
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 50

    def get_likes(self, obj):
        return len(obj.like.all())


    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)



admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment,CommentAdmin)
