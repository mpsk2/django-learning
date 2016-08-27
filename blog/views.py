from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Post


@method_decorator(login_required, 'dispatch')
class PostCreate(CreateView):
    model = Post
    success_url = reverse_lazy('home')
    fields = ['title', 'content']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:post_list')


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 10
