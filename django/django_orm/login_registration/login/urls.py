from django.urls import path
from . import views
urlpatterns = [
    path('register',views.register), 
    path('login',views.login),
    path('',views.index),
    path('success',views.success),
    path('logout',views.logout)
    #path('admin/', admin.site.urls),
]
