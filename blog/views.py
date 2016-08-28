from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from .models import Post, Comment


class CreatorRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.created_by != self.request.user:
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)


@method_decorator(login_required, 'dispatch')
class PostCreate(generic.CreateView):
    model = Post
    success_url = reverse_lazy('blog:post_list')
    fields = ['title', 'content']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        return super().form_valid(form)


class PostList(generic.ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 10


@method_decorator(login_required, 'dispatch')
class PostDelete(CreatorRequiredMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')
    context_object_name = 'post'


@method_decorator(login_required, 'dispatch')
class PostUpdate(CreatorRequiredMixin, generic.UpdateView):
    model = Post
    success_url = reverse_lazy('blog:post_list')
    fields = ['title', 'content']


class PostDetail(generic.DetailView):
    model = Post
    context_object_name = 'post'


@method_decorator(login_required, 'dispatch')
class CommentCreate(generic.CreateView):
    model = Comment
    fields = ['content']
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.post = get_object_or_404(Post, id=self.kwargs['post_id'])
        return super().form_valid(form)
