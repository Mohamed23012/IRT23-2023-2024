from django import forms
from Enseignant.models import Category


class CategoryForm(forms.ModelForm):  
    class Meta:  
        model = Category  
        fields = [
            'nom',
            'photo',
        ]
        widgets = {
            'nom': forms.TextInput(attrs={ 'class': 'form-control' }),
            'photo': forms.FileInput(attrs={'class':'form-control'}),
        }