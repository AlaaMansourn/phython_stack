from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('create',views.write_to_db),

    
    
]