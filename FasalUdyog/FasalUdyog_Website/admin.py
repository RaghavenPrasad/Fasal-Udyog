from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(center)
admin.site.register(farmer_deposits_stock)
admin.site.register(handler)
admin.site.register(manager)
admin.site.register(orders)
admin.site.register(stock_center)
admin.site.register(stock_farmer)
admin.site.register(stock_total)
admin.site.register(store)
admin.site.register(store_has_orders)
admin.site.register(farmer)
# admin.site.register(state)