from django.urls import path
from .views import product_page
urlpatterns = [
    path("<str:slug>",product_page,name="product_page")
]
