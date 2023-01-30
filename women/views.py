from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response

from .models import WomenPost
from .serializers import WomenSerializer

# Create your views here.


class PostList(viewsets.ModelViewSet):
    queryset = WomenPost.objects.all()
    serializer_class = WomenSerializer















# class PostList(viewsets.ViewSet):
#     def list(self, request):
#         queryset = WomenPost.objects.all()
#         serializer = WomenSerializer(queryset, many=True)
#         return Response(serializer.data)











#
# # get
# class PostList(generics.ListAPIView):
#     queryset = WomenPost.objects.all()
#     serializer_class = WomenSerializer
#
#
# # post
# class PostCreate(generics.CreateAPIView):
#     queryset = WomenPost.objects.all()
#     serializer_class = WomenSerializer
#
#
# # get and post
# class PostListCreate(generics.ListCreateAPIView):
#     queryset = WomenPost.objects.all()
#     serializer_class = WomenSerializer
#
#
# # retrieve-- you have to add <int:pk> to urls as it just reads selected item
# class PostRetrieve(generics.RetrieveAPIView):
#         queryset = WomenPost.objects.all()
#         serializer_class = WomenSerializer
#
#
# # delete -- it deletes the chosen item but it does not show
# class PostDestroy(generics.DestroyAPIView):
#     queryset = WomenPost.objects.all()
#     serializer_class = WomenSerializer
#
