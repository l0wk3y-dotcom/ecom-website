from django.shortcuts import render
from products.models import Product

def index(request):
    products=Product.objects.all()
    print(request.user)
    context={"products":products}
    return render(request,'home/home.html',context)

