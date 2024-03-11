from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

# This will be all of the django paths that the blog post app will access
urlpatterns = [
    # This is the path that will take you to the blog app home page.
    # At this time, this page is set as the homepage for the entire project. THIS WILL CHANGE AS WEBSITE GROWS!!!
    path('', PostListView.as_view(), name='blog-home'),
    # Creating a route with the id of the post is part of the route.
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # Creating a new post
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    # This will allow the user to update their posts in their blog
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
     # This will allow the user to delete their posts in their blog
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # This is the path that will take you to the blog app about page.
    path('about/', views.about, name='blog-about')
]