from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Post


@method_decorator(login_required, 'dispatch')
class PostCreate(CreateView):
    model = Post
    success_url = reverse_lazy('home')
    fields = ['title', 'content']
