from django.contrib import admin
from .models import OrderDetail, Product, Review, Mediators

# Register your models here.

admin.site.register(OrderDetail)
admin.site.register(Mediators)
admin.site.register(Product)
admin.site.register(Review)