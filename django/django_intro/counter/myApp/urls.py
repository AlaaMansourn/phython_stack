from django.urls import path     
from . import views
urlpatterns = [
    path('', views.display_visit),
    path('destroy_session',views.clear_session)
    
]