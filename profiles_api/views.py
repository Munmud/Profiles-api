from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from . import serializers


class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSearilizer

    def get(self,request, format=None):
        """Return a list of APIview feature"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional django view',
            'Gives you most application over your application logic',
            'Is mapped manully to URLs',
        ]

        return Response( {'message':'Hello', 'an_apiview':an_apiview} )


    def post(self,request):
        '''Create a hello message with our name'''

        serializers = self.serializer_class(data=request.data)

        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            message = f'Hello {name}'
            return Response( {'message' : message })
        else : 
            return Response(
                serializers.errors ,
                status=status.HTTP_400_BAD_REQUEST 
            )


    def put(self,request,pk=None):
        '''Handle updating an object, pk= primary key'''
        return Response({'method' : 'PUT'})
    

    def patch(self,request,pk=None):
        '''Handle partial update of an object '''
        return Response({'method' : 'PATCH'})
    

    def delete(self, request,pk=None):
        '''Delete an object'''
        return Response({'method' : 'DELETE'})
        

class HelloViewSet(viewsets.ViewSet):
    '''Test API View set'''
    serializer_class = serializers.HelloSearilizer

    def list(self,request):
        '''return a Hello message'''
        a_view_set = [
            'Uses action for (list, create, retrive, update, partial_update, destroy)',
            'Automatically maps to URLS using Routers',
            'Provide more Functionality with less code',
        ]

        return Response({'message':a_view_set})
    

    def create(self,request):
        '''Create a new Hello Message'''
        serializer = self.serializer_class(data=request.data)

        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            message = f'Hello {name}'
            return Response( {'message' : message })
        else : 
            return Response(
                serializers.errors ,
                status=status.HTTP_400_BAD_REQUEST 
            )


    def retrive(self,request, pk=None):
        '''Handle getting an object by its id'''
        return Response({'HTTP Method': 'GET'})
    
    
    def update(self,request, pk=None):
        '''Handle updating an object'''
        return Response({'HTTP Method': 'UPDATE'})
    
    
    def partial_update(self,request, pk=None):
        '''Handle updating part of an object'''
        return Response({'HTTP Method': 'PATCH'})

    def destroy(self,request, pk=None):
        '''Handle destroying an object'''
        return Response({'HTTP Method': 'DELETE'})
    

     