from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied

from .models import Post


class CreatorRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.created_by != self.request.user:
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)


@method_decorator(login_required, 'dispatch')
class PostCreate(CreateView):
    model = Post
    success_url = reverse_lazy('blog:post_list')
    fields = ['title', 'content']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        return super().form_valid(form)


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 10


class PostDelete(CreatorRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')
    context_object_name = 'post'


class PostUpdate(CreatorRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy('blog:post_list')
    fields = ['title', 'content']


class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'

