from django.conf.urls import url
from . import views

app_name = 'objects'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='objects'),
    url(r'^/display_object/(?P<pk>[0-9]+)', views.DetailView.as_view(), name='display_object'),
]
