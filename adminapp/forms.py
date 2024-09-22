from django import forms
from homeapp.models import Tbl_Category


class Category_Form(forms.ModelForm):
    class Meta:
        model = Tbl_Category
        fields = '__all__'

        widgets = {

            'category_image': forms.FileInput(attrs={'required': 'false'}),
        }
