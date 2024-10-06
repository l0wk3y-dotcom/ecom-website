from django.db import models
from Base.models import BaseModel
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from Base.emails import send_email_activation_mail
from products.models import Product, Color, Size
import uuid
   



class Profile(BaseModel):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile")
    email_is_verified=models.BooleanField(default=False)
    email_token=models.CharField(max_length=100,null=True,blank=True)
    profile_picture=models.ImageField(upload_to="profile", null=True, blank=True)

    def get_cart_count(self):
        count = CartItems.objects.filter(cart__user=self.user, cart__is_paid=False).count()
        print(count)
        return count
        

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    email=instance.email
    email_token=str(uuid.uuid4())
    Profile.objects.create(email_token=email_token,user=instance)
    send_email_activation_mail(email=email,email_token=email_token)



class Cart(BaseModel):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="cart")
    is_paid=models.BooleanField(default=False)

    def __str__(self):
        return f"user: {self.user.username} | paid: {self.is_paid}"


class CartItems(BaseModel):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="cart_items")
    item=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    color=models.ForeignKey(Color,on_delete=models.SET_NULL,null=True,blank=True)
    size=models.ForeignKey(Size,on_delete=models.SET_NULL,null=True,blank=True)

    def get_total_price(self):
        total_price=[]
        item_price=self.item.price
        total_price.append(item_price)
        if self.color:
            color_price=self.color.price
            total_price.append(color_price)
        if self.size:
            size_price=self.size.price
            total_price.append(size_price)
        return sum(total_price)
        



    
