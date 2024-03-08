from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import models
from profiles_api import serializers
from profiles_api import permissions


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


class HelloViewSet(viewsets.ViewSet):
    """Test ViewSet"""
    serializer_class=serializers.HelloSerializer  # resposible for inputbox 

    def list(self, request):
        """Returns a hello msg"""
        a_viewset=[
            'Uses actions (list, create, retrieve, update, partial_update)',
            'automatically maps to urls using routers',
            'provides more functionality with less code'
        ]
        return Response({'message': 'hello!', 'a_viewset': a_viewset})
    
    def create(self, request):
        """Create a new hello msg"""
        serializer =self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message =f'hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )
        

    def retrieve(self,request,pk=None):
        """handle getting an object by its ID"""
        return Response({'http_method':'get'})
    
    def update(self,request,pk=None):
        """handle updating of an object"""
        return Response({'http_method':'put'})
    
    def partial_update(self,request,pk=None):
        """handle updating part of an object"""
        return Response({'http_method':'patch'})
    
    def destroy(self,request,pk=None):
        """handle removing of an object"""
        return Response({'http_method':'delete'})
    
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class =serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)
