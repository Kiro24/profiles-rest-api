from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer

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

    
    def post(self, request):
        """Returns a hello message with supplied in post request"""

        serialzier = self.serializer_class(data=request.data)

        if serialzier.is_valid():
            name = serialzier.validated_data.get('name')
            message = f'Hello, {name}'
            return Response({'message': message})
        else:
            return Response(serialzier.errors, 
            status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """Full update of an object according to supplid pk (id)"""
        return Response({'method':'PUT'})

    
    def patch(self, request, pk=None):
        """Partial update of an object according to supplid pk (id)"""
        return Response({'method':'PATCH'})

    
    def delete(self, request, pk=None):
        """delets an object according to supplid pk (id)"""
        return Response({'method':'DELETE'})