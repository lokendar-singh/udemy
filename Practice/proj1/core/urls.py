from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'^$',views.firstpage,name='firstpage'),
    url(r'^userform/',views.call_form,name='userform'),
    url(r'^genform/',views.call_form2,name='genform'),
]
