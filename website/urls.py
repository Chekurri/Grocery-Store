from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('cart/', views.cart),
    path('shipping/', views.shipping ),
    path('payment/', views.payment, name="payment"),
    path('summary/', views.summary, name ="summary"),
    path('confirm/', views.confirm, name='confirm'),
]