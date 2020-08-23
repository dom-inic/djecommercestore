from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('addnewitem/', views.addnewitem, name='addnewitem'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('cart', views.cartpage, name='cart'),
]
