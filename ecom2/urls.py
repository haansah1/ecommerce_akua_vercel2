from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path('register', views.register, name = "register"),
    path('login', views.login, name = "login"),
    path('logout', views.logout, name ="logout"),
    path('cart', views.cart, name ="cart"),
    path('checkout', views.checkout, name ="checkout"),
    path('update_item', views.update_item, name ="update_item"),
    path('processOrder', views.processOrder, name ="processOrder"),
    path('search', views.search, name ="search"),
    path('post/<str:pk>', views.post, name="post"),
    path('detail/<int:product_id>/', views.product_detail, name='detail'),
    path('bikini', views.bikini, name='bikini'),
    path('top', views.top, name='top'),
    path('combo', views.combo, name='combo'),    
    path('sweater', views.sweater, name='sweater'),

    
]
