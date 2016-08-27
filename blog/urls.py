from django.conf.urls import url

from .views import PostCreate, PostList

urlpatterns = [
    # posts
    url(r'^new$', PostCreate.as_view(), name='post_new'),
    url(r'^$', PostList.as_view(), name='post_list'),
]