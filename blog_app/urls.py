from django.urls import path
from .views import BlogHomePage, BlogDetailViewPage, BlogNewPostPage, BlogUpdateViewPage, BlogDeleteViewPage, BlogAboutPage

urlpatterns = [
    path('', BlogHomePage.as_view(), name='home'),
    path('post/new/', BlogNewPostPage.as_view(), name='new_post'),
    path('post_detail/<int:pk>/', BlogDetailViewPage.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', BlogUpdateViewPage.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogDeleteViewPage.as_view(), name='post_delete'),
    path('post/about', BlogAboutPage.as_view(), name='about'),
]
