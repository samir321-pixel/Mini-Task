from django.db import models
from phone_field import PhoneField
import uuid


class Mediators(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = PhoneField(blank=False)



class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_id = models.UUIDField(default=uuid.uuid4, editable=False)
    link = models.URLField(max_length=252, blank=False)
    price = models.IntegerField()
    mediators = models.ForeignKey("Order.Mediators", on_delete=models.CASCADE)



class OrderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey("User.CustomUser", on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey("Order.Product", on_delete=models.CASCADE)
    mediator = models.ForeignKey("Order.Mediators", on_delete=models.CASCADE)
    order_id= models.UUIDField(default=uuid.uuid4, editable=False)
    order_amount= models.IntegerField()
    delivery_datetime = models.DateTimeField(auto_now=True)



class Review(models.Model):
    user = models.ForeignKey("User.CustomUser", on_delete=models.CASCADE, null=True, blank=True)
    order_detail = models.ForeignKey("Order.OrderDetail", on_delete=models.CASCADE)
    review = models.CharField(max_length=100, blank=False)
    star_rating = models.IntegerField()

