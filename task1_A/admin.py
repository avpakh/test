from django.contrib import admin

from .models import Category
from .models import Product
from .models import Person

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Person)

