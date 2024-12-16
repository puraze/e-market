from django.db.models import Max, Min
from .models import Product

max_price = Product.objects.aggregate(Max('price'))
min_price = Product.objects.aggregate(Min('price'))