<<<<<<< HEAD
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
=======
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from Enseignant.forms import CategoryForm, EnseignantForm
from Enseignant.models import Category, Enseignant
from .forms import RechercheEnseignantForm

# Create your views here.
def ajoutercategory(request):  
    if request.method == "POST" :  
        formcategory = CategoryForm(request.POST, request.FILES)  
        if formcategory.is_valid():  
             
                formcategory.save()  
                return redirect('list_category')
                print("ah")  
            
        else :
            print ("ah1")   
    else:  
        formcategory = CategoryForm() 
        print("err")
        
    return render(request,'ajoutercategory.html',{'formcategory':formcategory}) 

def list_category(request):  
    categoryts = Category.objects.all()  
    return render(request,"liste_category.html",{'categoryts':categoryts})  

def modifier(request, id):  
    category = Category.objects.get(id=id)  
    if request.method == 'POST':
        formcategory = CategoryForm(request.POST, instance=category)  
        if formcategory.is_valid():  
            formcategory.save()  
            return redirect("list_category")  
    else:
        formcategory= CategoryForm(instance=category)
        print("ah1")

    return render(request, 'modifier_category.html', {'category': category, 'formcategory': formcategory})
 
def suprimer(request, id):
    category = get_object_or_404(Category, id=id)
    return render(request, 'suprimer.html', {'category': category})

     

     
def destroycategory(request, id):
        category = Category.objects.get(id=id)  
        category.delete()  
        return redirect("list_category" )   


def ajouterenseignant(request):  
    if request.method == "POST" :  
        form = EnseignantForm(request.POST, request.FILES)  
        if form.is_valid():  
             
                form.save()  
                return redirect('liste_enseignant')
                print("ah")  
            
        else :
            print ("ah1")   
    else:  
        form = EnseignantForm() 
        print("err")
        
    return render(request,'ajouterenseignant.html',{'form':form}) 
def liste_enseignant(request):  
    enseignants = Enseignant.objects.all()  
    return render(request,"liste_enseignants.html",{'enseignants':enseignants})   


def update(request, id):  
    enseignant = Enseignant.objects.get(id=id)  
    if request.method == 'POST':
        form = EnseignantForm(request.POST, request.FILES, instance=enseignant)  
        if form.is_valid():  
            form.save()  
            return redirect("liste_enseignant")  
    else:
        form = EnseignantForm(instance=enseignant)
        print("ah1")

    return render(request, 'modifier_enseignant.html', {'enseignant': enseignant, 'form': form})

def confirm_delete(request, id):
    enseignant = get_object_or_404(Enseignant, id=id)
    return render(request, 'confirme.html', {'enseignant': enseignant})

     

     
def destroy(request, id):
        enseignant = Enseignant.objects.get(id=id)  
        enseignant.delete()  
        return redirect("liste_enseignant" )  
def recherche_enseignant(request):
    form = RechercheEnseignantForm(request.GET or None)
    enseignants = Enseignant.objects.all()
    
    if form.is_valid():
        name = form.cleaned_data.get('name')
        sexe = form.cleaned_data.get('sexe')
        experience = form.cleaned_data.get('experience')

        if name:
            enseignants = enseignants.filter(name__icontains=name)
        if sexe:
            enseignants = enseignants.filter(sexe=sexe)
        if experience:
            enseignants = enseignants.filter(experience__icontains=experience)

    return render(request, 'recherche.html', {'form': form, 'enseignants': enseignants})



from django.db.models import Count

def graphiques_enseignants(request):
    # Données pour le graphique d'âge
    enseignants = Enseignant.objects.all()
    ages = [enseignant.age for enseignant in enseignants]

    # Données pour le graphique de sexe
    sexes_count = Enseignant.objects.values('sexe').annotate(nombre=Count('sexe'))
    sexes = {sex['sexe']: sex['nombre'] for sex in sexes_count}

    # Données pour le graphique de catégorie
    categories_count = Enseignant.objects.values('categories__nom').annotate(total=Count('categories'))
    categories = {cat['categories__nom']: cat['total'] for cat in categories_count}

    # Données pour le graphique de niveau
    niveaux_count = Enseignant.objects.values('niveau').annotate(total=Count('niveau'))
    niveaux = {niveau['niveau']: niveau['total'] for niveau in niveaux_count}

    return render(request, 'graphiques_enseignants.html', {
        'ages': ages,
        'sexes': sexes,
        'categories': categories,
        'niveaux': niveaux
    })

import csv
def import_enseignant_csv(request):
    if request.method == "GET":
        return render(request, "csv_import.html", {'oname': "Enseignant", 'opath': "enseignant"})
    try:
        object_list = []
        csv_file = request.FILES["formFile"]
        file_data = csv_file.read().decode("latin-1")  # Utilisation de l'encodage latin-1
        lines = file_data.split("\n")
        for line in lines:
            if line.strip():  # Vérifier si la ligne n'est pas vide
                fields = line.split(",")
                if len(fields) == 13:  # Vérifier si la ligne contient le nombre attendu de champs
                    ob = Enseignant()
                    ob.name = fields[0]
                    ob.prenom = fields[1]
                    ob.email = fields[2]
                    ob.contact = fields[3]
                    ob.age = int(fields[4])
                    ob.sexe = fields[5]
                    ob.experience = fields[6]
                    ob.cartier = fields[7]
                    ob.niveau = fields[8]
                    ob.status = fields[9]
                    ob.cv = fields[10]  # Assurez-vous que le fichier est déjà téléchargé dans le répertoire de médias
                    ob.photo = fields[11]  # Assurez-vous que le fichier est déjà téléchargé dans le répertoire de médias
                    ob.save()
                    object_list.append(ob)

                    # Gérer la relation ManyToMany avec Category
                    categories_ids = fields[12].split(";")
                    categories = Category.objects.filter(id__in=categories_ids)
                    ob.categories.add(*categories)
                else:
                    print("Nombre de champs incorrect dans la ligne du fichier CSV")
            else:
                print("Ligne vide ignorée")

    except Exception as e:
        print("Error! Unable to upload file. " + repr(e))
        return HttpResponseRedirect(reverse("enseignant_import"))

    return HttpResponseRedirect(reverse("liste_enseignant"))
def export_enseignants_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="enseignants.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nom', 'Prénom', 'Email', 'Contact', 'Age', 'Sexe', 'Experience', 'Cartier', 'Niveau', 'CV', 'Photo', 'Categories', 'Status'])

    enseignants = Enseignant.objects.all()
    for enseignant in enseignants:
        categories = ';'.join([categorie.nom for categorie in enseignant.categories.all()])
        writer.writerow([
            enseignant.name,
            enseignant.prenom,
            enseignant.email,
            enseignant.contact,
            enseignant.age,
            enseignant.sexe,
            enseignant.experience,
            enseignant.cartier,
            enseignant.niveau,
            enseignant.cv.name if enseignant.cv else '',  # Utilisez le nom du fichier de CV s'il existe, sinon une chaîne vide
            enseignant.photo.name if enseignant.photo else '',  # Utilisez le nom du fichier de photo s'il existe, sinon une chaîne vide
            categories,
            enseignant.status,
        ])

    return response
>>>>>>> main
