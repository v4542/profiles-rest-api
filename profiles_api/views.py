from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test APIVIEW"""

    def get(self, request, format=None):
        """Returns a list of apiview features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, dekete)', 'Is similar to a traditional Django view', 'gives you the most control over you application logic ', 'Is mapped manually to URLs'
        ]

        return Response({'message': 'hello!', 'an_apiview': an_apiview})