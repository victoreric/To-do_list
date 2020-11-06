from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('list/',include ('list.urls', namespace="list")),
    path('',views.index, name='home'),
    path('admin/', admin.site.urls),
    
    
]
