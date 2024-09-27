from django import forms
from .models import Item , Category

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'ingredients', 'image', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter item name'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter ingredients'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {'name': 'نام',
                  'ingredients': 'محتویات',
                  'image': 'تصویر',
                  'category': 'دسته بندی',

                  }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category title'}),
        }
