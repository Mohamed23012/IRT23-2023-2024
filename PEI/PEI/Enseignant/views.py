from django.shortcuts import render, redirect, get_object_or_404
from .models import Enseignant, EnseignantHistory
from .forms import EnseignantSignupForm, EnseignantUpdateForm , AgeFilterForm

def enseignant_signup(request):
    if request.method == 'POST':
        form = EnseignantSignupForm(request.POST, request.FILES)
        if form.is_valid():
            enseignant = form.save()
            return redirect('profil_enseignant', enseignant_id=enseignant.id)
    else:
        form = EnseignantSignupForm()
    return render(request, 'signup.html', {'form': form})

def mettre_a_jour_enseignant(request, enseignant_id):
    enseignant = get_object_or_404(Enseignant, id=enseignant_id)
    if request.method == 'POST':
        form = EnseignantUpdateForm(request.POST, request.FILES, instance=enseignant)
        if form.is_valid():
            history = EnseignantHistory(
                enseignant=enseignant,
                name=enseignant.name,
                prenom=enseignant.prenom,
                email=enseignant.email,
                contact=enseignant.contact,
                age=enseignant.age,
                sexe=enseignant.sexe,
                cv=enseignant.cv,
                photo=enseignant.photo,
                experience=enseignant.experience,
                cartier=enseignant.cartier,
                niveau=enseignant.niveau,
                category=enseignant.category,
                status=enseignant.status
            )
            history.save()
            form.save()
            return redirect('profil_enseignant', enseignant_id=enseignant.id)
    else:
        form = EnseignantUpdateForm(instance=enseignant)
    histories = enseignant.histories.all()
    return render(request, 'mettre_a_jour_enseignant.html', {'form': form, 'histories': histories})

def profil_enseignant(request, enseignant_id):
    enseignant = get_object_or_404(Enseignant, id=enseignant_id)
    return render(request, 'profil_enseignant.html', {'enseignant': enseignant})

def afficher_historique_enseignant(request, enseignant_id):
    enseignant = get_object_or_404(Enseignant, id=enseignant_id)
    histories = enseignant.histories.all()
    return render(request, 'historique_enseignant.html', {'histories': histories})


def enseignant_list(request):
    form = AgeFilterForm(request.GET)
    enseignants = Enseignant.objects.all()
    
    if form.is_valid():
        age_min = form.cleaned_data.get('age_min')
        age_max = form.cleaned_data.get('age_max')
        if age_min is not None:
            enseignants = enseignants.filter(age__gte=age_min)
        if age_max is not None:
            enseignants = enseignants.filter(age__lte=age_max)
    
    return render(request, 'recherche_age.html', {'enseignants': enseignants, 'form': form})
