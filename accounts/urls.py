from django.urls import path
from . import views

urlpatterns = [
     path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('category',views.category,name="category"),
    path('signin',views.signin,name="signin"),
    path('cart',views.cart,name="cart"),
    path('contact',views.contact,name="contact"),\
    path('home',views.home,name="home"),
    path('account',views.account,name="account"),
    path('reg', views.reg, name='reg'),
 
    path('logout/', views.logout_view, name='logout'),
    path('men_wear',views.men_wear,name="men_wear"),
    path('rahul',views.rahul,name="rahul"),
  
path('product/<int:id>/', views.product_detail, name='product_detail'),
path('product/<int:product_id>/add/', views.add_to_cart, name='add_to_cart'),
 
]
