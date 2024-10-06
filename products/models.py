from django.db import models
from Base.models import BaseModel
from django.utils.text import slugify

class Category(BaseModel):
    category_name=models.CharField(max_length=30)
    slug=models.SlugField(unique=True,null=True,blank=True)
    category_image=models.ImageField(upload_to='Category_images')
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name

class Color(BaseModel):
    color_name=models.CharField(max_length=100)
    price=models.IntegerField()

    def __str__(self):
        return self.color_name
    

class Size(BaseModel):
    size_name=models.CharField(max_length=10)
    price=models.IntegerField()

    def __str__(self):
        return self.size_name
    
    

class Product(BaseModel):
    product_name=models.CharField(max_length=100)
    product_description=models.CharField(max_length=1000)
    slug=models.SlugField(unique=True,null=True,blank=True)
    price=models.IntegerField(default=500)
    size=models.ManyToManyField(Size, blank=True)
    color=models.ManyToManyField(Color, blank=True)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,related_name='products', null=True)

    def get_product_by_size(self, size):
        Total_price=self.price+Size.objects.get(size_name=size).price + 200
        print(Total_price)
        return Total_price
        

    def save(self,*args, **kwargs):
        self.slug=slugify(self.product_name)
        super(Product,self).save(*args, **kwargs)

    def __str__(self):
        return self.product_name
    


class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE, related_name='product_images')
    product_image=models.ImageField(upload_to='product')

