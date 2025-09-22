# backend/search/admin.py
from django.contrib import admin
from .models import Domain, Article, SERPResult

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'created_at', 'updated_at')
    search_fields = ('url',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'domain', 'status', 'last_checked_at', 'updated_at')
    list_filter = ('status', 'domain')
    search_fields = ('title', 'url')
    raw_id_fields = ('domain',)

@admin.register(SERPResult)
class SERPResultAdmin(admin.ModelAdmin):
    list_display = ('article', 'search_engine', 'rank', 'checked_at')
    list_filter = ('search_engine',)
    search_fields = ('article__title',)
    raw_id_fields = ('article',)