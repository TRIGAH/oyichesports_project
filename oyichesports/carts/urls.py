from django.conf.urls import url
from .views import cart_home,update_cart

app_name='carts'
urlpatterns = [
     url(r'^$', cart_home, name='home'),
     url(r'^update_cart/$', update_cart, name='update_cart'),
]