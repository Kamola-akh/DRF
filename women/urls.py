from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/create/', PostCreate.as_view()),
    path('posts/retrieve/<int:pk>', PostRetrieve.as_view()),
    path('posts/destroy/<int:pk>', PostDestroy.as_view()),
    path('posts/list-create/', PostListCreate.as_view()),
    path('posts/create', PostCreate.as_view()),

]
