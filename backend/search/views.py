from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics # generics をインポート
from .models import Domain, Article # Articleを追加
from .serializers import DomainSerializer, ArticleSerializer # ArticleSerializerを追加

# 動作確認用のAPIビュー
class ExampleView(APIView):
    def get(self, request, *args, **kwargs):
        """
        GETリクエストが来た時にJSONを返すサンプル
        """
        data = {
            "message": "Hello from search-san API!",
            "status": "ok"
        }
        return Response(data, status=status.HTTP_200_OK)

class DomainListCreateView(generics.ListCreateAPIView):
    """
    ドメインの一覧取得(GET)と新規登録(POST)を行うAPIビュー
    """
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer

class DomainRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    特定のドメイン1件の詳細取得(GET)・更新(PUT/PATCH)・削除(DELETE)を行うAPIビュー
    """
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer

class ArticleListCreateView(generics.ListCreateAPIView):
    """
    記事の一覧取得(GET)と新規登録(POST)を行うAPIビュー
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    特定の記事1件の詳細取得(GET)・更新(PUT/PATCH)・削除(DELETE)を行うAPIビュー
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
