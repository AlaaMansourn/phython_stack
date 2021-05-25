from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index),
    path('shows/new',views.index1),
    path('process',views.index2),
    path('shows/<int:id>',views.index3), 
    path('shows',views.tvShows),
    path('shows/<int:id>/edit',views.showEdit), 
    path('update',views.updateShow),
    path('shows/<int:id>/delete',views.deleteShow)
    #path('admin/', admin.site.urls),
]