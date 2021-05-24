from django.urls import path
from . import views
urlpatterns = [
    path('login',views.login), 
    path('',views.index),
    #path('admin/', admin.site.urls),
]
