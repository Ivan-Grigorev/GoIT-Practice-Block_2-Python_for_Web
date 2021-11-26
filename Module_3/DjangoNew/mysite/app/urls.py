from django.urls import path
from . import views

urlpatterns = [
       path("about/", views.AboutView.as_view(), name="about"),
       path("post/<int:pk>", views.PostDetailView.as_view(), name="post_detail"),
       path("", views.PostListView.as_view(), name='post_list'),
       path("post/new", views.CreatePostView.as_view(), name="post_form"),
       path("post/<int:pk>/edit", views.UpdatePostView.as_view(), name="update"),
       path("post/<int:pk>/delete", views.DeletePostView.as_view(), name="post_delete")
    ]

