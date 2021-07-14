from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""

    def get(self,request, format=None):
        """Return a list of APIview feature"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional django view',
            'Gives you most application over your application logic',
            'Is mapped manully to URLs',
        ]

        return Response( {'message':'Hello', 'an_apiview':an_apiview} )
