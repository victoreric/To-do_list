from django.conf.urls import url
from  .import views

app_name='mysite'

urlpatterns=[
    url('create/', views.create, name='create'),
    url('/',views.list, name='index'),
]
