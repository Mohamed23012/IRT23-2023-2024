from django.db import models



class Teacher(models.Model):
    nom_complet = models.CharField(max_length=255)
    adresse_email = models.EmailField()
    numero_telephone = models.CharField(max_length=15)
    matiere_principale = models.CharField(max_length=100)
    competences_specifiques = models.TextField()
    diplomes = models.TextField()
    experience_professionnelle = models.TextField()
    disponibilite = models.CharField(max_length=255)
    certification = models.CharField(max_length=100, blank=True, null=True)
   


class Student(models.Model):
    nom_complet = models.CharField(max_length=255)
    adresse_email = models.EmailField()
    numero_telephone = models.CharField(max_length=15)
    niveau_scolaire = models.CharField(max_length=100)
    matiere_interet = models.CharField(max_length=100)
    competences_recherchees = models.TextField()
  




    
