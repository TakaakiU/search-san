from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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