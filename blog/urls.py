from django.conf.urls import url

from .views import PostCreate, PostList, PostDelete, PostUpdate, PostDetail, CommentCreate

urlpatterns = [
    # posts
    url(r'^post/new$', PostCreate.as_view(), name='post_new'),
    url(r'^post/$', PostList.as_view(), name='post_list'),
    url(r'^post/edit/(?P<pk>\d+)$', PostUpdate.as_view(), name='post_edit'),
    url(r'^post/delete/(?P<pk>\d+)$', PostDelete.as_view(), name='post_delete'),
    url(r'^post/(?P<pk>\d+)$', PostDetail.as_view(), name='post_detail'),

    # comments
    url(r'^post/(?P<post_id>\d+)/comment/new$', CommentCreate.as_view(), name='comment_new'),
]