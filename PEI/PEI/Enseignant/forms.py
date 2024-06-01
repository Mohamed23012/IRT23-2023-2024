from django import forms
from .models import Enseignant 
from .models import Category  

class CategoryForm(forms.ModelForm):  
    class Meta:  
        model = Category  
        fields = [
           
            'nom',
        ]
        widgets = {
            'nom': forms.TextInput(attrs={ 'class': 'form-control' }),
        }
class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['name', 'prenom', 'email', 'contact', 'age', 'sexe', 'cv', 'photo', 'experience', 'cartier', 'niveau', 'category', 'status']


class EnseignantSignupForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['name', 'prenom', 'email', 'contact', 'age', 'sexe', 'cv', 'photo', 'experience', 'cartier', 'niveau', 'category', 'status']

class EnseignantUpdateForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['name', 'prenom', 'email', 'contact', 'age', 'sexe', 'cv', 'photo', 'experience', 'cartier', 'niveau', 'category', 'status']
from django import forms

class AgeFilterForm(forms.Form):
    age_min = forms.IntegerField(label='Âge minimum', required=False)
    age_max = forms.IntegerField(label='Âge maximum', required=False)
