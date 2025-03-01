from django.contrib import admin

from articles.models import Article, Comment


# Register your models here.
class CommentInLine(admin.TabularInline):
    extra = 0
    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]
    list_display = ['title', 'body', 'author']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
