from django.urls import path

from .views import PostDetailView, PostFromCategory, PostListView

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("post/<str:slug>/", PostDetailView.as_view(), name="post_detail"),
    path("category/<str:slug>/", PostFromCategory.as_view(), name="post_by_category"),
]
