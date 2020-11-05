from django.conf.urls import url
from  .import views

app_name='mysite'

urlpatterns=[
    url('',views.index, name='home'),
]
