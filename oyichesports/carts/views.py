from django.shortcuts import render, redirect
from shop.models import Shop
from .models import Cart
# Create your views here.
# def cart_create(request):
#     cart_obj = Cart.objects.create(user=None)
#     print('New Cart Created')
#     return cart_obj


def cart_home(request):
    
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    shop = cart_obj.shop_items.all()
    total = 0
    for x in shop:
        total +=x.price
    print(total)
    cart_obj.total = total
    cart_obj.save()
    context = {
        'object_list' : foods,
        'total':total
    }
    
    
  
    return render(request,'carts/add_to_cart.html',context) 
    # if cart_id is None:
    #     cart_obj = cart_create()
    #     request.session['cart_id'] = cart_obj.id
    #     print('New Cart Created')
    # else:
    # qs = Cart.objects.filter(id=cart_id)
    # if qs.count()==1: 
    #     print('Card ID Exists')  
    #     cart_obj = qs.first()
    #     if request.user.is_authenticated and cart_obj.user is None:
    #         cart_obj.user = request.user
    #         cart_obj.save()
    # else:
    #     cart_obj = Cart.objects.new(user=request.user)
    #     request.session['cart_id'] = cart_obj.id

def update_cart(request):
    print(request.POST)
    shop_item_id = request.POST.get('shop_item_id')
    if shop_item_id is not None:
        try:
            shop_item_obj = Shop.objects.get(id=shop_item_id)
        except Shop.DoesNotExist:   
                print("It has been added")
                return redirect('page:index') 
        cart_obj, new_obj = Cart.objects.new_or_get(request)
                # return redirect(product_obj.get_absolute_url())
        if shop_obj in cart_obj.shop_item.all():
            cart_obj.shop_item.remove(shop_obj)
          
        else: 
            cart_obj.shop_item.add(shop_obj)
        request.session['cart_items'] = cart_obj.shop_item.count()   

    return redirect('cart:home')
