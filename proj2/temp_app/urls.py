#from django.conf import url
from django.urls import path,re_path
from temp_app import views

app_name = 'sam_app'

urlpatterns = [
    re_path(r'^other/$',views.other,name='url_other'),
    re_path(r'^relative/$',views.relative_view,name='url_relative'),
]
