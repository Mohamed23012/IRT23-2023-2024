from django.shortcuts import get_object_or_404, redirect, render

from Enseignant.forms import CategoryForm
from Enseignant.models import Category

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