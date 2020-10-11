from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Tag
from .forms import PostForm, TagForm


class PostsList(ListView):
    """
    Main Posts List, Search, Pagination View

    Search by fields: title (Post model), body (Post model) and title (Tag model).
    """
    model = Post
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get('search', '')
        if search_query:
            posts = Post.objects.filter(
                Q(title__icontains=search_query) | Q(body__icontains=search_query)
                | Q(tags__title__icontains=search_query))
            # Objects per search page
            self.pagination(context, 3, posts)
            if context['object_list']:
                context['search_message_success'] = 'Posts containing ' + '"' + search_query + '":'
            else:
                context['search_message_no_matches'] = 'No posts containing' + ' "' + search_query + '" found.'
        # All posts with pagination
        else:
            posts = Post.objects.all()
            # Objects per posts page
            self.pagination(context, 3, posts)
        return context

    def pagination(self, context, number_obj_per_page, posts):
        """
        Main pagination method (for all posts objects or searched post objects)
        """
        search_query = self.request.GET.get('search', '')
        paginator = Paginator(posts, number_obj_per_page)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context['is_paginated'] = page.has_other_pages()
        if page.has_previous() and not search_query:
            context['prev_url'] = '?page={}'.format(page.previous_page_number())
        elif page.has_previous() and search_query:
            print(search_query)
            context['prev_url'] = '?search={}&page={}'.format(search_query, page.previous_page_number())
        else:
            context['prev_url'] = ''
        if page.has_next() and not search_query:
            context['next_url'] = '?page={}'.format(page.next_page_number())
        elif page.has_next() and search_query:
            context['next_url'] = '?search={}&page={}'.format(search_query, page.next_page_number())
        else:
            context['next_url'] = ''
        context['object_list'] = page


class PostDetail(DetailView):
    model = Post
    template = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pointer for applying the appropriate style to the template
        context['detail'] = True
        return context


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create_form.html'
    success_url = reverse_lazy('posts_list_url')
    login_url = 'posts_list_url'


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_update_form.html'
    login_url = 'posts_list_url'


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete_form.html'
    success_url = reverse_lazy('posts_list_url')
    login_url = 'posts_list_url'


class TagsList(ListView):
    model = Tag
    template_name = 'blog/tags_list.html'


class TagDetail(DetailView):
    model = Tag
    template = 'blog/tag_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pointer for applying the appropriate style to the template
        context['detail'] = True
        return context


class TagCreate(LoginRequiredMixin, CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'blog/tag_create.html'
    success_url = reverse_lazy('tags_list_url')
    login_url = 'tags_list_url'


class TagUpdate(LoginRequiredMixin, UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'blog/tag_update_form.html'
    login_url = 'tags_list_url'


class TagDelete(LoginRequiredMixin, DeleteView):
    model = Tag
    template_name = 'blog/tag_delete_form.html'
    success_url = reverse_lazy('tags_list_url')
    login_url = 'tags_list_url'
