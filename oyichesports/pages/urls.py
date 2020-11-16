from django.urls import path
from django.conf.urls import url
from .views import  about, contact, page_404,checkout,gallery,team,news,results,add_player


app_name='pages'
urlpatterns = [

    # url(r'^$', index, name='index'),
    url(r'^about/$', about, name='about'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^checkout/$', checkout, name='checkout'),
    url(r'^gallery/$', gallery, name='gallery'),
    url(r'^news/$', news, name='news'),
    url(r'^team/$', team, name='team'),
    url(r'^add_player/$', add_player, name='add_player'),
    url(r'^results/$', results, name='results'),
    url(r'^404/$', page_404, name='404'),
    
   
]