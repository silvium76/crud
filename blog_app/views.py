from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy


class BlogHomePage(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'


class BlogDetailViewPage(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogNewPostPage(CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = ['title', 'author', 'body']


class BlogUpdateViewPage(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteViewPage(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
