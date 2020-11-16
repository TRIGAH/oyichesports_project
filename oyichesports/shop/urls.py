
from django.conf.urls import url
from .views import shop_page, ShopDetailView 

app_name='shop'
urlpatterns = [
url(r'^shop/$', shop_page, name='shop'),
 
]
