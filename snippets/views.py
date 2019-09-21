from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from snippets.serializers import UserSerializer
from rest_framework import permissions 
from django.contrib.auth.models import User
from snippets.permissions import IsOwnerOrReadOnly
#from rest_framework.views import APIView
#from rest_framework import status
#from rest_framework import mixins
from rest_framework import generics
#from rest_framework.response import Response
#from django.http import Http404


# Create your views here.
class SnippetList(generics.ListCreateAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
	
# class SnippetList(APIView):
# 	"""
# 	List all code snippets, or create a new snippet.
# 	"""
# 	def get(self, request, format=None):
# 		snippets = Snippet.objects.all()
# 		serializer = SnippetSerializer(snippets, many=True)
# 		return Response(serializer.data)

# 	def post(self, request, format=None):	
# 		serializer = SnippetSerializer(data=data.request)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer		
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
	
# class SnippetDetail(APIView):
# 	"""
# 	Retreive, update or delete a code snippet.
# 	"""
# 	def get_object(self, pk):
# 		try:
# 			snippet = Snippet.objects.get(pk=pk)
# 		except Snippet.DoesNotExist:
# 			return Response(status=status.HTTP_404_NOT_FOUND)

# 	def get(self, request, pk, format=None):
# 		snippet = self.get_object(pk)
# 		serializer = SnippetSerializer(snippet)
# 		return Response(serializer.data)	

# 	def put(self, response, pk, format=None):
# 		snippet = self.get_object(pk)
# 		serializer = SnippetSerializer(snippet, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
# 	def delete(self, request, pk, format:None):
# 		snippet = self.get_object(pk)
# 		snippet.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)	

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer						