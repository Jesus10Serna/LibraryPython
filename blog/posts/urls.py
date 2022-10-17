from django.urls import path
from .views import PostList, PostDetail, PostViewSet, UserList, UserDetail
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("posts", PostViewSet, basename="posts")
urlpatterns = [
    path("<int:pk>/", UserList.as_view(), name="todo_detail"),
    path("", UserDetail.as_view(), name="todo_list"),
    path("<int:pk>/", PostDetail.as_view(), name="todo_detail"),
    path("", PostList.as_view(), name="todo_list")
] + router.url
