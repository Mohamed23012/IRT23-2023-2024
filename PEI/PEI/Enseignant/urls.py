<<<<<<< HEAD
from django.urls import path
from . import views 

urlpatterns = path('signup/', views.enseignant_signup, name='signup'),
              path('mettre_a_jour/<int:enseignant_id>/', views.mettre_a_jour_enseignant,       name='mettre_a_jour_enseignant'),
              path('profil/<int:enseignant_id>/', views.profil_enseignant, name='profil_enseignant'),
              path('historique/<int:enseignant_id>/', views.afficher_historique_enseignant, name='historique_enseignant'),
              path('enseignants/', views.enseignant_list, name='enseignant_list'),
 ]
=======
from . import views 
from django.urls import path

urlpatterns = [

    path('ajoutercategory',views.ajoutercategory, name='ajoutercategory'),
    path('listecategory', views.list_category, name='list_category'),
    path('modifier/<int:id>', views.modifier, name='modifier'), 
    path('suprimer/<int:id>', views.suprimer, name='suprimer'),
    path('destroycategory/<int:id>', views.destroycategory, name='destroycategory'),
    path('ajouterenseignant',views.ajouterenseignant, name='ajouterenseignant'),
    path('liste_enseignant', views.liste_enseignant, name='liste_enseignant'), 
    path('update/<int:id>', views.update, name='update'), 
    path('delete/<int:id>', views.confirm_delete, name='confirm_delete'),
    path('destroy/<int:id>', views.destroy, name='destroy'),
    path('graph/', views.graphiques_enseignants, name='graphiques_enseignants'),
    path('import/enseignant', views.import_enseignant_csv, name='enseignant_import'),
    path('export/enseignant', views.export_enseignants_csv, name='export_enseignants_csv'),
    path('rechercher/', views.recherche_enseignant, name='recherche_enseignant'),



]
>>>>>>> main
