from django.shortcuts import render
from rest_framework import generics
from .models import WomenPost
from .serializers import WomenSerializer
# Create your views here.


# get
class PostList(generics.ListAPIView):
    queryset = WomenPost.objects.all()
    serializer_class = WomenSerializer


# post
class PostCreate(generics.CreateAPIView):
    queryset = WomenPost.objects.all()
    serializer_class = WomenSerializer


# get and post
class PostListCreate(generics.ListCreateAPIView):
    queryset = WomenPost.objects.all()
    serializer_class = WomenSerializer


# retrieve-- you have to add <int:pk> to urls as it just reads selected item
class PostRetrieve(generics.RetrieveAPIView):
        queryset = WomenPost.objects.all()
        serializer_class = WomenSerializer


# delete -- it deletes the chosen item but it does not show
class PostDestroy(generics.DestroyAPIView):
    queryset = WomenPost.objects.all()
    serializer_class = WomenSerializer

