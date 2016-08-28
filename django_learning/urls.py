from django.conf import settings
from django.views.static import serve
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    # base view with no processing
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),

    url(r'^admin/', admin.site.urls),

    # blog with posts and comments
    url(r'^blog/', include('blog.urls', namespace='blog')),

    # tutorial app
    url(r'^polls/', include('polls.urls', namespace='polls')),

    url(r'^accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]