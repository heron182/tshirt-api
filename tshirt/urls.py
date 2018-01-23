from django.conf.urls import url
from tshirt import views

urlpatterns = [
    url(r'^$', views.tshirt_list),
    url(r'(?P<pk>[0-9]+)/$', views.tshirt_detail),
]
