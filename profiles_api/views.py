from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
        