from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('<int:id>',views.booktemplate),
    path('process',views.gettitle),
    path('addauthor',views.addauthor),
    path('author',views.index4),
    path('author/<int:id>',views.authortemplate),
    path('process2',views.authorToadd),
    path('addbook',views.addbookto), 
    #path('admin/', admin.site.urls),
]
