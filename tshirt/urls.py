from django.conf.urls import url
from tshirt import views

urlpatterns = [
    url(r'^$', views.tshirt_list),
]
