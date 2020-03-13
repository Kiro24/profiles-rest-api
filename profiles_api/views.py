from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):

    def get(self, requerst, format=None):
        """Returns a list of APIView freatures"""

        users = [
            'kiro',
            'mark',
            'bicha'
        ]

        return Response({
            'message': 'hello there!!',
            'users': users})