from django.db import models
from django.db import models

# Create your models here.
class Category(models.Model) :

    nom = models.CharField(max_length=150)
    # image = models.ImageField(upload_to='images/')


    class Meta:  
        db_table = "category"

        
class Enseignant(models.Model):  
    name = models.CharField(max_length=100)  
    prenom = models.CharField(max_length=100) 
    email = models.EmailField()  
    contact = models.CharField(max_length=15) 
    age = models.PositiveIntegerField()
    sexe = models.CharField(max_length=100)
    cv =models.ImageField(upload_to='images/')
    photo = models.ImageField(upload_to='images/')
    experience = models.CharField(max_length=100)
    cartier = models.CharField(max_length=100)
    niveau = models.CharField(max_length=100)
    category=models.ForeignKey(Category, on_delete=models.PROTECT  )

    

   
    class Meta:  
        db_table = "enseignant"
