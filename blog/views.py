from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Post


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


# TODO(mps): ACCEPTS ANYONE TO DELETE!!!!
class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')
    context_object_name = 'post'
