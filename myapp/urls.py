from django.conf.urls import url

from myapp import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^home/$', views.index, name="home"),
    url(r'^market/(\d+)/(\d+)/(\d+)/$', views.market, name="market"),
    url(r'^cart/$', views.cart, name="cart"),
    url(r'^mine/$', views.mine, name="mine"),
    url(r'^login/$', views.login, name="login"),
    url(r'^registe/$', views.registe, name="registe"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^checkaccount/$', views.checkaccount, name="checkaccount"),

]
