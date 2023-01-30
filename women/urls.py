from django.urls import path
from .views import *


urlpatterns = [
    path('posts/', PostList.as_view({'get': 'list'})),
    path('posts/<int:pk>/', PostList.as_view({'post': 'update'}))


]
