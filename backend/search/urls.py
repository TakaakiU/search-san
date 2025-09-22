from django.urls import path
from . import views # searchアプリのviews.pyからビューをインポート

urlpatterns = [
    # 動作確認用のサンプルエンドポイント
    # http://localhost:8000/api/example/ でアクセスできるようにします
    path('example/', views.ExampleView.as_view(), name='example'),
    # ドメインの一覧取得・新規登録用エンドポイント
    path('domains/', views.DomainListCreateView.as_view(), name='domain-list-create'),
    # Domain APIs
    path('domains/<int:pk>/', views.DomainRetrieveUpdateDestroyView.as_view(), name='domain-detail'),
    # Article APIs
    path('articles/', views.ArticleListCreateView.as_view(), name='article-list-create'),
    path('articles/<uuid:pk>/', views.ArticleRetrieveUpdateDestroyView.as_view(), name='article-detail'),
]