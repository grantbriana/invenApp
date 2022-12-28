from django import forms
from django.forms import ModelForm
from .models import Item

class AddItem(forms.Form):
    id = forms.CharField(help_text="Enter Item ID")
    name = forms.CharField(help_text="Enter Item Name")
    inventory = forms.IntegerField(help_text="Enter Item Quantity")


class AddItemModelForm(ModelForm):
    class Meta:
        model = Item
        fields = ['id','name','inventory']