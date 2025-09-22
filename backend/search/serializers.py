# backend/search/serializers.py (新規作成)

from rest_framework import serializers
from .models import Domain, Article, SERPResult

class DomainSerializer(serializers.ModelSerializer):
    """
    Domainモデル用のシリアライザ
    """
    class Meta:
        model = Domain
        fields = ['id', 'url', 'created_at', 'updated_at'] # APIで送受信するフィールドを指定
        read_only_fields = ['id', 'created_at', 'updated_at'] # 読み取り専用フィールドを指定

class ArticleSerializer(serializers.ModelSerializer):
    """
    Articleモデル用のシリアライザ
    """
    class Meta:
        model = Article
        fields = ['id', 'domain', 'url', 'title', 'status', 'last_checked_at', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class SERPResultSerializer(serializers.ModelSerializer):
    """
    SERPResultモデル用のシリアライザ
    """
    class Meta:
        model = SERPResult
        fields = ['id', 'article', 'search_engine', 'rank', 'checked_at']
        read_only_fields = ['id']
