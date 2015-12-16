from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
                       url(r'^$', views.hello, name='hello'),
                       url(r'about/', views.about, name='about'),
                       url(r'add_category', views.add_category,
                           name='add_category'),
                       )
