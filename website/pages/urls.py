from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^constitution/$', views.constitution, name='constitution'),
    url(r'^events/$', views.events, name='events'),
    url(r'^event/(?P<pk>\d+)/$', views.event_detail, name='event_detail'),
    url(r'^news/$', views.news, name="news"),
    url(r'^wus/$', views.wus, name="wus"),
    url(r'^quote/$', views.quote, name="quote"),
    url(r'^gallery/$', views.gallery, name="gallery"),
    url(r'^committee/$', views.committee, name='committee'),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^privacy_notice/$', views.privacy_notice, name='privacy_notice'),
]
