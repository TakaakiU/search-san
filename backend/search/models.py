# backend/search/models.py
import uuid
from django.db import models
from django.utils import timezone 

# Create your models here.
class Domain(models.Model):
    """
    ユーザーが登録するドメイン情報を管理するモデル
    """
    url = models.CharField(max_length=255, unique=True, help_text="登録するドメインのURL (例: example.com)")
    created_at = models.DateTimeField(auto_now_add=True, help_text="作成日時")
    updated_at = models.DateTimeField(auto_now=True, help_text="更新日時")

    def __str__(self):
        return self.url

    class Meta:
        ordering = ['-created_at'] # 作成日時の降順で並び替える

class Article(models.Model):
    """
    ドメインに属する記事情報を管理するモデル
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, related_name='articles', help_text="所属するドメイン")
    url = models.URLField(unique=True, help_text="記事のURL")
    title = models.CharField(max_length=255, blank=True, help_text="記事のタイトル")
    last_checked_at = models.DateTimeField(null=True, blank=True, help_text="最後に順位をチェックした日時")
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', 'アクティブ'
        INACTIVE = 'INACTIVE', '非アクティブ'
        ARCHIVED = 'ARCHIVED', 'アーカイブ済み'
    
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.ACTIVE,
        help_text="記事の状態"
    )

    def __str__(self):
        return self.title or self.url

    class Meta:
        ordering = ['-created_at']
        unique_together = [['domain', 'url']]

class SERPResult(models.Model):
    """
    記事ごとの検索順- 位結果を記録するモデル
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='serp_results', help_text="対象の記事")
    
    class SearchEngine(models.TextChoices):
        GOOGLE = 'GOOGLE', 'Google'
        BING = 'BING', 'Bing'
        # 必要に応じて他の検索エンジンも追加
    
    search_engine = models.CharField(
        max_length=10,
        choices=SearchEngine.choices,
        help_text="検索エンジン"
    )
    
    rank = models.PositiveIntegerField(help_text="検索順位")
    checked_at = models.DateTimeField(default=timezone.now, help_text="計測日時")

    def __str__(self):
        # article.titleが空の場合も考慮
        article_identifier = self.article.title or self.article.url
        return f"{article_identifier} - {self.search_engine}: {self.rank}位"

    class Meta:
        ordering = ['-checked_at']
        # 1つの記事に対して、同じ日時の同じ検索エンジンの結果は1つだけ
        unique_together = [['article', 'search_engine', 'checked_at']]
