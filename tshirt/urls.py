from django.conf.urls import url

from tshirt import views

urlpatterns = [
    url(r'^$', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    url(r'^color/$', views.ColorList.as_view(), name=views.ColorList.name),
    url(r'^color/(?P<pk>[0-9]+)/$',
        views.ColorListDetail.as_view(),
        name=views.ColorListDetail.name),
    url(r'^category/$',
        views.CategoryList.as_view(),
        name=views.CategoryList.name),
    url(r'^category/(?P<pk>[0-9]+)/$',
        views.CategoryListDetail.as_view(),
        name=views.CategoryListDetail.name),
    url(r'^brand/$', views.BrandList.as_view(), name=views.BrandList.name),
    url(r'^brand/(?P<pk>[0-9]+)/$',
        views.BrandListDetail.as_view(),
        name=views.BrandListDetail.name),
    url(r'^tshirt/$', views.TshirtList.as_view(), name=views.TshirtList.name),
    url(r'^tshirt/(?P<pk>[0-9]+)/$',
        views.TshirtListDetail.as_view(),
        name=views.TshirtListDetail.name),
]
