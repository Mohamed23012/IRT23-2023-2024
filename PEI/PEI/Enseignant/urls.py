from . import views 
from django.urls import path

urlpatterns = [
    path('ajoutercategory',views.ajoutercategory, name='ajoutercategory'),
    path('listecategory', views.list_category, name='list_category'),



]