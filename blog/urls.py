from django.conf.urls import url
from django.views.generic.base import TemplateView

from .views import PostCreate

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='blog/index.html'), name='home'),

    # posts
    url(r'^new$', PostCreate.as_view(), name='post_new')
]