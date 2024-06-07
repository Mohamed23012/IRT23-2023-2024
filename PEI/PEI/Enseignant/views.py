from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from Enseignant.forms import CategoryForm, EnseignantForm, RechercheEnseignantForm
from Enseignant.models import Category, Enseignant

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
    if request.method == "POST":
        form = EnseignantForm(request.POST, request.FILES)
        if form.is_valid():
            enseignant = form.save()  # Ne sauvegarde pas encore dans la base de données
            enseignant.password = make_password(form.cleaned_data['password'])  # Hache le mot de passe
            enseignant.save()  # Sauvegarde maintenant avec le mot de passe haché
            return redirect('liste_enseignant')
            print("ah")
        else:
            print("ah1")
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
from django.contrib.auth.hashers import make_password
import csv

def import_enseignant_csv(request):
    if request.method == "GET":
        return render(request, "csv_import.html", {'oname': "Enseignant", 'opath': "enseignant"})
    
    try:
        csv_file = request.FILES["formFile"]
        file_data = csv_file.read().decode("latin-1")  # Utilisation de l'encodage latin-1
        lines = file_data.split("\n")
        
        for line in lines:
            if line.strip():  # Vérifier si la ligne n'est pas vide
                fields = line.split(",")
                if len(fields) == 15:  # Vérifier si la ligne contient le nombre attendu de champs
                    username = fields[0]
                    password = fields[1] if fields[1] else "default_password"  # Mot de passe par défaut si vide
                    email = fields[2]
                    name = fields[3]
                    prenom = fields[4]
                    contact = fields[5]
                    age = int(fields[6])
                    sexe = fields[7]
                    experience = fields[8]
                    cartier = fields[9]
                    niveau = fields[10]
                    status = fields[11]
                    cv = fields[12]  # Assurez-vous que le fichier est déjà téléchargé dans le répertoire de médias
                    photo = fields[13]  # Assurez-vous que le fichier est déjà téléchargé dans le répertoire de médias
                    categories_ids = fields[14].split(";")
                    
                    enseignant = Enseignant(
                        username=username,
                        email=email,
                        name=name,
                        prenom=prenom,
                        contact=contact,
                        age=age,
                        sexe=sexe,
                        experience=experience,
                        cartier=cartier,
                        niveau=niveau,
                        status=status,
                        cv=cv,
                        photo=photo,
                    )
                    enseignant.set_password(password)  # Pour hacher le mot de passe
                    enseignant.save()
                    
                    categories = Category.objects.filter(id__in=categories_ids)
                    enseignant.categories.add(*categories)
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
    writer.writerow(['username', 'password', 'email', 'name', 'prenom', 'contact', 'age', 'sexe', 'experience', 'cartier', 'niveau', 'status', 'cv', 'photo', 'categories'])

    enseignants = Enseignant.objects.all()
    for enseignant in enseignants:
        categories = ';'.join([str(categorie.id) for categorie in enseignant.categories.all()])
        writer.writerow([
            enseignant.username,
            enseignant.password,  # Mot de passe vide pour la sécurité
            enseignant.email,
            enseignant.name,
            enseignant.prenom,
            enseignant.contact,
            enseignant.age,
            enseignant.sexe,
            enseignant.experience,
            enseignant.cartier,
            enseignant.niveau,
            enseignant.status,
            enseignant.cv.name if enseignant.cv else '',  # Utilisez le nom du fichier de CV s'il existe, sinon une chaîne vide
            enseignant.photo.name if enseignant.photo else '',  # Utilisez le nom du fichier de photo s'il existe, sinon une chaîne vide
            categories,
        ])

    return response

from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html', {'admin_name': request.user.username})

def home_view(request):

    return render(request,'index.html')

from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)
    return redirect('login')  # Redirige vers la page de login après la déconnexion

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

from django.shortcuts import render, get_object_or_404
from .models import Category, Enseignant

def categories_list(request):
    categories = Category.objects.all() 
    return render(request, 'categories_list.html', {'categories': categories})
def enseignants_list(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    # Filtrer les enseignants dont le statut est "confirmé"
    enseignants = category.enseignant_set.filter(status='confirmé')
    return render(request, 'enseignants_list.html', {'category': category, 'enseignants': enseignants})