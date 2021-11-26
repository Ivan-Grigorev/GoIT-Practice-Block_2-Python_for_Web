from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .models import Post
from .forms import PostAddForm


class AboutView(TemplateView):
    template_name = 'app/about.html'


class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    queryset = Post.objects.order_by('-creation_date')


class PostDetailView(DetailView):
    model = Post


class CreatePostView(CreateView):
    form_class = PostAddForm
    model = Post
    success_url = reverse_lazy('post_list')


class UpdatePostView(UpdateView):
    form_class = PostAddForm
    model = Post
    success_url = reverse_lazy('post_list')


class DeletePostView(DeleteView):
    model = Post
    template_name = 'app/post_delete.html'
    success_url = reverse_lazy('post_list')
