from django.contrib import admin

# Register your models here.
from .models import Cart, Restaurant, User, Item

admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(Cart)