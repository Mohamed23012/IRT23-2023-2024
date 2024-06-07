from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Enseignant , Category
# Register your models here.
# admin.site.register(User)
admin.site.register(Enseignant)
admin.site.register(Category)