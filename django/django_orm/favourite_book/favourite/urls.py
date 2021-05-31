from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('login',views.login),
    
    path('add_book',views.addbook),
    path('logout',views.logout),
    path('view_book',views.viewbook)
    #path('admin/', admin.site.urls),
]
