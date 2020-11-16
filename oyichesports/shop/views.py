from django.shortcuts import render
from .models import Shop
from carts.models import Cart
from django.views.generic import ListView,DetailView
# Create your views here.
def shop_page(request):
    shop = Shop.objects.all()
    context = {
       'shop':shop,
       
       
      
    }
    return render(request,'shop/shop_fullwidth.html',context)


class ShopDetailView(DetailView):
    queryset = Shop.objects.all()
    template_name = 'shop/shop_fullwidth.html'
    def get_context_data(self, *args, **kwargs):
         context = super(ShopDetailView, self).get_context_data(*args, **kwargs)
         cart_obj, new_obj = Cart.objects.new_or_get(self.request)
         context['cart'] = cart_obj
         return context

# class FoodListView(ListView):
#     template_name = 'food/food.html'

#     def get_queryset(self, *args, **kwargs):
#         request = self.request
#         return Food.objects.all()