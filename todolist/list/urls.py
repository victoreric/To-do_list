from django.conf.urls import url
from  .import views

app_name='mysite'

urlpatterns=[
    url('detail/(?P<detail_id>[0-9]+)', views.detail, name='detail'),
    url('cross_off/(?P<list_id>[0-9]+)', views.cross_off, name='cross_off'),
    url('uncross/(?P<list_id>[0-9]+)', views.uncross, name='uncross'),
    url('search/', views.search, name='search'),
    url('del/(?P<delete_id>[0-9]+)', views.delete, name='delete'),
    url('update/(?P<update_id>[0-9]+)', views.update, name='update'),
    url('create/', views.create, name='create'),
    url('',views.list, name='index'),
]
