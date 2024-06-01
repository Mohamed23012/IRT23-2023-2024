from django.urls import path
from . import views 

urlpatterns = path('signup/', views.enseignant_signup, name='signup'),
              path('mettre_a_jour/<int:enseignant_id>/', views.mettre_a_jour_enseignant,       name='mettre_a_jour_enseignant'),
              path('profil/<int:enseignant_id>/', views.profil_enseignant, name='profil_enseignant'),
              path('historique/<int:enseignant_id>/', views.afficher_historique_enseignant, name='historique_enseignant'),
              path('enseignants/', views.enseignant_list, name='enseignant_list'),
 ]
