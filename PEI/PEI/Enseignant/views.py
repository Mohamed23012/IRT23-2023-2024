from django.shortcuts import render, redirect
from .forms import EnseignantSignUpForm
from django.contrib.auth.hashers import make_password

from django.contrib import messages

def enseignant_signup(request):
    if request.method == 'POST':
        form = EnseignantSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                enseignant = form.save(commit=False)
                enseignant.password = make_password(form.cleaned_data['password'])
                enseignant.save()
                return redirect('login')
            except Exception as e:
                messages.error(request, 'Erreur lors de la sauvegarde : {}'.format(e))
        else:
            messages.error(request, 'Le formulaire n’est pas valide.')
    else:
        form = EnseignantSignUpForm()
    return render(request, 'signup.html', {'form': form})
