from . import views 
from django.urls import path

urlpatterns = [
    path('ajoutercategory',views.ajoutercategory, name='ajoutercategory'),
    path('listecategory', views.list_category, name='list_category'),
    path('modifier/<int:id>', views.modifier, name='modifier'), 
    path('suprimer/<int:id>', views.suprimer, name='suprimer'),
    path('destroycategory/<int:id>', views.destroycategory, name='destroycategory'),



]