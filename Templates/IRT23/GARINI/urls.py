from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teachers/', views.teachers, name='teachers'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),  # URL pour la page de contact
    # Autres URL pour les autres vues
]
