from django.urls import path
from . import views
urlpatterns = [
    path('register',views.register), 
    path('login',views.login),
    
    path('success',views.wall),
    path('logout',views.logout),
    path('',views.wall),
    path('wall',views.wall)
    #path('admin/', admin.site.urls),
]