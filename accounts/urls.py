from django.urls import path
from .views import login_page, register_page, activate_email
from products.views import add_to_cart, cart_page, delete_cartitem
urlpatterns = [
    path('login/',login_page,name="login_page"),
    path('register/',register_page,name="register_page"),
    path('activate/<email_token>',activate_email,name="activate_email"),
    path('add_to_cart/<uid>',add_to_cart, name="add_to_cart"),
    path('cart/',cart_page,name="cart_page"),
    path('delete-cart-item/<uid>/',delete_cartitem,name="delete_cart_item")

]