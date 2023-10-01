from django.contrib import admin
from .models import Booking, Carousel, Cart, Category, Feedback, Product, UserProfile

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(UserProfile)
admin.site.register(Cart)
admin.site.register(Booking)
admin.site.register(Feedback)
admin.site.register(Carousel)