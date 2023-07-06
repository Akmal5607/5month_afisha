from django.contrib import admin
from posts.models import Post, Comment


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rate', 'created_date', 'modified_data')
    sortable_by = ('rate',)


admin.site.register(Post)
admin.site.register(Comment)
