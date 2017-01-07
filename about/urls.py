from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<work_id>[0-9]+)/$', views.work_detail, name='index'),
    url(r'^about/$', views.about, name='index'),
    url(r'^work/$', views.work, name='index'),
    url(r'^contact/$', views.contact, name='index'),
]
