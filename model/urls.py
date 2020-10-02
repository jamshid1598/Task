from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^download/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
]