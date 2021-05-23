from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('addninja',views.addNinja),
    path('adddojo',views.adddojo),
    path('test',views.test), 
    #path('admin/', admin.site.urls),
]