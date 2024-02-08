from django.contrib import admin
from .models import Book, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'user', 'book', 'datetime_created', 'recommend', 'is_active')


admin.site.register(Book)
# admin.site.register(Comment, CommentAdmin)
