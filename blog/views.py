from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from .models import Post
from .forms import PostForm
from django.db.models import Count, Max
from django.shortcuts import render
from django.contrib.auth.models import User


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_edit.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class StatisticsView(TemplateView):
    template_name = "blog/statistics.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        authors = Post.objects.values('author__username').annotate(cnt=Count('author__username'), lst=Max('published_date'))
        context['authors'] = authors
        return context


