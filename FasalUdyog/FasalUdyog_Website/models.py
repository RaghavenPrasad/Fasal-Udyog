from django.db import models

# Create your models here.
class center(models.Model):
    center_id = models.CharField(max_length=45)
    handler_name = models.CharField(max_length=45)
    village_name = models.CharField(max_length=45)
    handler_id = models.CharField(max_length=45)

    def __str__(self):
        return self.center_id

class farmer_deposits_stock(models.Model):
    farmer_id = models.CharField(max_length=45)
    item_id = models.CharField(max_length=45)
    item_name = models.CharField(max_length=45)
    quantity = models.CharField(max_length=45)

    def __str__(self):
        return self.farmer_id

class handler(models.Model):
    handler_id = models.CharField(max_length=45)
    handler_name = models.CharField(max_length=45)
    handler_contact = models.CharField(max_length=45)
    handler_address = models.CharField(max_length=45)

    def __str__(self):
        return self.handler_id

class manager(models.Model):
    manager_id = models.CharField(max_length=45)
    manager_name = models.CharField(max_length=45)
    manager_contact = models.CharField(max_length=45)
    manager_address = models.CharField(max_length=45)
    manager_pass = models.CharField(max_length=45)

    def __str__(self):
        return self.manager_id

class orders(models.Model):
    order_id = models.CharField(max_length=45)  # IntegerField
    item_id = models.CharField(max_length=45)
    item_name = models.CharField(max_length=45)
    quantity = models.CharField(max_length=45)
    store_address = models.CharField(max_length=45)
    zip = models.CharField(max_length=45)
    locality = models.CharField(max_length=45)

    def __str__(self):
        return self.order_id

class stock_center(models.Model):
    item_id = models.CharField(max_length=45)   # IntegerField
    quantity = models.CharField(max_length=45)   # IntegerField
    msp = models.CharField(max_length=45)   # IntegerField
    item_name = models.CharField(max_length=45)
    center_id = models.CharField(max_length=45)

    def __str__(self):
        return self.item_id

class stock_farmer(models.Model):
    item_id = models.CharField(max_length=45)
    quantity = models.CharField(max_length=45)
    msp = models.CharField(max_length=45)
    item_name = models.CharField(max_length=45)

    def __str__(self):
        return self.item_id

class stock_total(models.Model):
    item_id = models.CharField(max_length=45)   # IntegerField
    msp = models.CharField(max_length=45)   # IntegerField
    quantity = models.CharField(max_length=45)   # IntegerField
    value = models.CharField(max_length=45)
    item_name = models.CharField(max_length=45)
    center_id = models.CharField(max_length=45)

    def __str__(self):
        return self.item_id

class store(models.Model):
    store_id = models.CharField(max_length=45)
    district_name = models.CharField(max_length=45)
    handler_id = models.CharField(max_length=45)
    handler_name = models.CharField(max_length=45)
    locality = models.CharField(max_length=45)
    zip = models.CharField(max_length=45)
    store_address = models.CharField(max_length=45)
    manager_id = models.CharField(max_length=45)
    GSTIN = models.CharField(max_length=45)

    def __str__(self):
        return self.store_id

class store_has_orders(models.Model):
    order_id = models.CharField(max_length=45)   # IntegerField
    store_id = models.CharField(max_length=45)
    item_name = models.CharField(max_length=45)
    item_id = models.CharField(max_length=45)
    quantity = models.CharField(max_length=45)
    orders_has_storecol = models.CharField(max_length=45)

    def __str__(self):
        return self.order_id

class farmer(models.Model):
    farmer_id = models.CharField(max_length=45)
    farmer_name = models.CharField(max_length=45)
    aadhaar_id = models.CharField(max_length=45)
    father_name = models.CharField(max_length=45)
    village_name = models.CharField(max_length=45)
    category = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)

    def __str__(self):
        return self.farmer_id

# class state(models.Model):
#     name = models.CharField(max_length=40)

#     def __str__(self):
#         return self.name
    
# class farmer(models.Model):
#     username = models.CharField(max_length=20)
#     aadhar = models.IntegerField()
#     store = models.IntegerField()
#     state = models.ForeignKey(state, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.username