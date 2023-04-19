from django import forms
from django.forms import ModelForm
from .models import farmer, orders

# Create a farmer form
class farmerForm(ModelForm):
    class Meta:
        model = farmer
        fields = '__all__'

        labels = {
            'farmer_id': 'Farmer ID',
            'farmer_name': 'Farmer Name',
            'aadhaar_id': 'Aadhaar Number',
            'father_name': 'Father Name',
            'village_name': 'Village Name',
            'category': 'Category',
            'gender': 'Gender',
        }

        widgets = {
            'farmer_id': forms.TextInput(attrs={'class': 'form-control'}),
            'farmer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'aadhaar_id': forms.TextInput(attrs={'class': 'form-control'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control'}),
            'village_name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
        }

class orderForm(ModelForm):
    class Meta:
        model = orders
        fields = ('item_id', 'item_name', 'quantity', 'store_address', 'zip', 'locality')

        labels = {
            'item_id': 'Item ID',
            'item_name': 'Item Name',
            'quantity': 'Quantity',
            'store_address': 'Store Address',
            'zip': 'Zip Code',
            'locality': 'Locality',
        }

        widgets = {
            'item_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'item_name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'store_address': forms.TextInput(attrs={'class': 'form-control'}),
            'zip': forms.NumberInput(attrs={'class': 'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
        }

# from django import forms
# from django.forms import ModelForm
# from .models import farmer

# # Create a farmer form
# class farmerForm(ModelForm):
#     class Meta:
#         model = farmer
#         fields = '__all__'

#         labels = {
#             'username': 'Name',
#             'aadhar': 'Aadhar Number',
#             'store': 'Store Number',
#             'state': 'State',
#         }

#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control'}),
#             'aadhar': forms.NumberInput(attrs={'class': 'form-control'}),
#             'store': forms.NumberInput(attrs={'class': 'form-control'}),
#             'state': forms.Select(attrs={'class': 'form-select'}),
#         }