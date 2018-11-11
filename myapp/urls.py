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

    url(r'^addcart/$', views.addcart, name='addcart'),  # 添加购物车
    url(r'^subcart/$', views.subcart, name='subcart'),  # 购物车减操作

    url(r'^changecartstatus/$', views.changecartstatus, name='changecartstatus'),  # 购物车商品是否选中
    url(r'^generateorder/$', views.generateorder, name='generateorder'),    #下单
    url(r'^orderinfo/(\d+)/$', views.orderinfo, name='orderinfo'),    #订单详情
    url(r'changecartselect/$', views.changecartselect,name='changecartselect'), # 全选/取消全选

]
