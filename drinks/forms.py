from django import forms
from .models import Item
# the form is for item table in models.py

class ItemForm(forms.ModelForm):
    # inherite ModelForm class from django forms 
    class Meta:
        # meta class provides information about the class "ItemForm" itself
        model = Item
        # which model we are using
        fields = ['item_name','item_desc','item_price','item_image','item_ingredients']
        # fields for the form
