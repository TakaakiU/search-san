from django.urls import path
from . import views # searchアプリのviews.pyからビューをインポート

urlpatterns = [
    # 動作確認用のサンプルエンドポイント
    # http://localhost:8000/api/example/ でアクセスできるようにします
    path('example/', views.ExampleView.as_view(), name='example'),
]