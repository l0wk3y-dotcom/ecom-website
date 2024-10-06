from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Product, Size, Color
from accounts.models import Cart, CartItems

def product_page(request, slug):
    selected_size=request.GET.get("size")
    try:
        product=Product.objects.get(slug=slug)
    except  Exception as e:
        print(e)
        return HttpResponse("404 Not Found")
    context={"product":product}
    if selected_size:
        total_price=product.get_product_by_size(selected_size)
        context["total_price"]=total_price
    return render(request,'products/product_page.html',context)



def add_to_cart(request, uid):
    size_variant=request.GET.get("size")
    color_variant=request.GET.get("color")
    cart, _ = Cart.objects.get_or_create(user=request.user, is_paid=False)
    item=Product.objects.get(uid=uid)
    cart_item=CartItems.objects.create(cart=cart, item=item)
    if size_variant:
        cart_item.size=Size.objects.get(size_name=size_variant)
        cart_item.save()
    if color_variant:
        cart_item.color=Color.objects.get(color_name=color_variant)
        cart_item.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))


def cart_page(request):
    products=CartItems.objects.filter(cart__user=request.user, cart__is_paid=False)
    context={"items":products}
    return render(request,'accounts/cart_page.html',context)


def delete_cartitem(request, uid):
    cart_item=get_object_or_404(CartItems,uid=uid)
    cart_item.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))
    