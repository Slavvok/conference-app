from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^plan/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^plan/new/$', views.post_new, name='post_new'),
    url(r'^plan/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^plan/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
