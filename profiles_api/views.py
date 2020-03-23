from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from profiles_api import permissions
from django.contrib.auth import get_user_model

class UserProfileViewSet(viewsets.ModelViewSet):
    '''handles creating and updating profiles'''

    serializer_class = serializers.UserProfileSerializer
    queryset = get_user_model().objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)







# class HelloApiView(APIView):

#     serializer_class = serializers.HelloSerializer

#     def get(self, requerst, format=None):
#         """Returns a list of APIView freatures"""

#         users = [
#             'kiro',
#             'mark',
#             'bicha'
#         ]

#         return Response({
#             'message': 'hello there!!',
#             'users': users})

    
#     def post(self, request):
#         """Returns a hello message with supplied in post request"""

#         serialzier = self.serializer_class(data=request.data)

#         if serialzier.is_valid():
#             name = serialzier.validated_data.get('name')
#             message = f'Hello, {name}'
#             return Response({'message': message})
#         else:
#             return Response(serialzier.errors, 
#             status=status.HTTP_400_BAD_REQUEST)


#     def put(self, request, pk=None):
#         """Full update of an object according to supplid pk (id)"""
#         return Response({'method':'PUT'})

    
#     def patch(self, request, pk=None):
#         """Partial update of an object according to supplid pk (id)"""
#         return Response({'method':'PATCH'})

    
#     def delete(self, request, pk=None):
#         """delets an object according to supplid pk (id)"""
#         return Response({'method':'DELETE'})


# class HelloViewSet(viewsets.ViewSet):
#     """Test api viewset"""

#     serialzer_class = serializers.HelloSerializer

#     def list(self, request):
#         """return hello message"""
#         a_viewset = [
#             'providse more functionality with less code',
#             'CRUD operations',
#             'automatically maps urls using routers',
#         ]

#         return Response({
#             'message':'hello admin',
#             'viewset_capabilities': a_viewset})

#     def create(self, request):
#         '''Creates a new hello message'''

#         serializer = self.serialzer_class(data=request.data)

#         if serializer.is_valid():
#             name = serializer.validated_data.get('name')
#             message = f'Hello {name}.....!'

#             return Response({'message':message})
#         else:
#             return Response(
#                 serializer.errors,
#                 status.HTTP_400_BAD_REQUEST,
#             )

#     def retrieve(self, requset, pk=None):
#         '''Handles getting an object by its id'''
#         return Response({'http_method': 'GET'})

#     def update(self, requset, pk=None):
#         '''Handles updating an object by its id'''
#         return Response({'http_method': 'PUT'})

#     def partial_update(self, requset, pk=None):
#         '''Handles updating part of an object by its id'''
#         return Response({'http_method': 'PATCH'})

#     def destroy(self, requset, pk=None):
#         '''Handles deleting an object'''
#         return Response({'http_method': 'DELETE'})


