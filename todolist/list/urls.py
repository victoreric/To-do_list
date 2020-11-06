from django.conf.urls import url
from  .import views

app_name='mysite'

urlpatterns=[
    url('del/(?P<delete_id>[0-9]+)', views.delete, name='delete'),
    url('update/(?P<update_id>[0-9]+)', views.update, name='update'),
    url('create/', views.create, name='create'),
    url('',views.list, name='index'),
]
