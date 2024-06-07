from django.db import models

# Create your models here.
class Category(models.Model):
    nom = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='images/')

    class Meta:
        db_table = "category"
    def __str__(self):
        return self.nom       

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission

class Enseignant(AbstractUser):
    STATUS_CHOICES = (
        ('confirmé', 'Confirmé'),
        ('non confirmé', 'Non confirmé'),
    )

    name = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    sexe = models.CharField(max_length=100)
    cv = models.ImageField(upload_to='images/')
    photo = models.ImageField(upload_to='images/')
    experience = models.CharField(max_length=100)
    cartier = models.CharField(max_length=100)
    niveau = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)  # Relation ManyToMany avec Category
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='non confirmé')
    # Vos champs personnalisés ici
    groups = models.ManyToManyField(Group, related_name='enseignants_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='enseignants_permissions')

    class Meta:
        db_table = "enseignant"
