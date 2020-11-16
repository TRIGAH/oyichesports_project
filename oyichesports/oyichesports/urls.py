"""oyichesports URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.conf.urls import url,include
from django.contrib import admin
from shop.views import shop_page,ShopDetailView
from pages.views import about,contact,page_404,checkout,gallery,team,news,add_player
from accounts.views import login_page,register_page,guest_register_view,dashboard_page,logout_page
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
   url(r'^admin/', admin.site.urls),
    url(r'^$', home,name='home'),
    url(r'^contact/$', contact_page, name='contact'),
    url(r'^login/$', login_page, name='login'),
    url(r'^dashboard/$', dashboard_page, name='dashboard'),
    url(r'^register/guest/$', guest_register_view, name='guest_register'),
    # url(r'^checkout/address/create/$', checkout_address_create_view, name='checkout_address_create'),
    url(r'^register/$', register_page, name='register'),
    url(r'^logout/$', logout_page, name='logout'),
    # url(r'^bootstrap/$', TemplateView.as_view(template_name='bootstrap/example.html')),
    url(r'^shops/',include('shop.urls', namespace='shops')),
    url(r'^championships/',include('championships.urls', namespace='championships')),
    url(r'^pages/',include('pages.urls', namespace='pages')),
    url(r'^results/',include('results.urls', namespace='results')),
    url(r'^team/',include('team.urls', namespace='team')),
    url(r'^ticketing/',include('ticketing.urls', namespace='ticketing')),
    url(r'^cart/',include('carts.urls', namespace='cart')),
    # url(r'^search/',include('search.urls', namespace='search')),
]
if settings.DEBUG:
   urlpatterns =urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   urlpatterns =urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
