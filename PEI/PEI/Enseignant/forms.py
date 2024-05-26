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
            'name',
            'prenom',
            'email',
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
class RechercheEnseignantForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, label='Nom')
    prenom = forms.CharField(max_length=100, required=False, label='Prénom')
    email = forms.EmailField(required=False, label='Email')
    contact = forms.CharField(max_length=100, required=False, label='Contact')
    cartier = forms.CharField(max_length=100, required=False, label='Quartier')
    niveau = forms.CharField(max_length=100, required=False, label='Niveau')
    status = forms.ChoiceField(choices=[('confirmé', 'Confirmé')], required=False, label='Statut')
<<<<<<< HEAD
    
=======
>>>>>>> main
