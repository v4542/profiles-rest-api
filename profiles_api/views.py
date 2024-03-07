from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """Test APIVIEW"""

    serializer_class=serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of apiview features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, dekete)', 'Is similar to a traditional Django view', 'gives you the most control over you application logic ', 'Is mapped manually to URLs'
        ]

        return Response({'message': 'hello!', 'an_apiview': an_apiview})
    
    def post(self, request):
        """Create a hello msg with our name"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
                )
        
    def put(self,request,pk=None):
        """handle updating an object"""
        return Response({'method':'put'})
        
    def patch(self,request,pk=None):
        """handle a partial update of an object"""
        return Response({'method':'patch'})
            
    def delete(self,request,pk=None):
        """delete an object"""
        return Response({'method':'delete'})
