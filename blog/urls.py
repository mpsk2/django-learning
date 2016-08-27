from django.conf.urls import url

from .views import PostCreate, PostList, PostDelete, PostUpdate, PostDetail

urlpatterns = [
    # posts
    url(r'^new$', PostCreate.as_view(), name='post_new'),
    url(r'^$', PostList.as_view(), name='post_list'),
    url(r'^edit/(?P<pk>\d+)$', PostUpdate.as_view(), name='post_edit'),
    url(r'^delete/(?P<pk>\d+)$', PostDelete.as_view(), name='post_delete'),
    url(r'^(?P<pk>\d+)$', PostDetail.as_view(), name='post_detail'),
]