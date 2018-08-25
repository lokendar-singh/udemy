from django.conf.urls import url
from relurl import views

app_name = 'loki_app'

urlpatterns = [
    url(r'^relative/$',views.relurl,name='rel_url_name'),
    url(r'^other/$',views.other,name='other_name'),
]
