from django.db import models

# Create your models here.
class Category(models.Model):
    nom = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='images/')

    class Meta:
        db_table = "category"
