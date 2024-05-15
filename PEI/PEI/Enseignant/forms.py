from django import forms 
from Enseignant.models import Enseignant ,Category 
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
            'category',
            
            ] 
        widgets = {
            'name': forms.TextInput(attrs={ 'class': 'form-control' }),
            'prenom': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'contact': forms.TextInput(attrs={ 'class': 'form-control' }),
            'age': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'sexe': forms.TextInput(attrs={ 'class': 'form-control' }),
            'cv': forms.FileInput(attrs={'class':'form-control'}),
            'photo': forms.FileInput(attrs={'class':'form-control'}),
            'experience': forms.TextInput(attrs={ 'class': 'form-control' }),
            'cartier': forms.TextInput(attrs={ 'class': 'form-control' }),
            'niveau' : forms.TextInput(attrs={ 'class': 'form-control' }),
            'category': forms.TextInput(attrs={ 'class': 'form-control' }),

      }
        
class CategoryForm(forms.ModelForm):  
    class Meta:  
        model = Category  
        fields = [
           
            'nom',
        ]
        widgets = {
            'nom': forms.TextInput(attrs={ 'class': 'form-control' }),
        }


from django import forms
from .models import Enseignant

class EnseignantSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Enseignant
        fields = ['name', 'prenom', 'email', 'contact', 'age', 'sexe', 'cv', 'photo', 'experience', 'cartier', 'niveau', 'category']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Les mots de passe ne correspondent pas."
            )

# forms.py
from django import forms
from .models import Enseignant

class EnseignantUpdateForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['name', 'prenom', 'email', 'contact', 'age', 'sexe', 'cv', 'photo', 'experience', 'cartier', 'niveau', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
