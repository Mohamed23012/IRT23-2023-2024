from django import forms
from Enseignant.models import Category, Enseignant


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


class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = [
            'username',
            'password',
            'email',
            'name',
            'prenom',
            'contact',
            'age',
            'sexe',
            'cv',
            'photo',
            'experience',
            'cartier',
            'niveau',
            'categories',
            'status',
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'sexe': forms.TextInput(attrs={'class': 'form-control'}),
            'cv': forms.FileInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'experience': forms.TextInput(attrs={'class': 'form-control'}),
            'cartier': forms.TextInput(attrs={'class': 'form-control'}),
            'niveau': forms.TextInput(attrs={'class': 'form-control'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }    