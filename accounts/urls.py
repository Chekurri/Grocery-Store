from django.urls import path
from . import views

urlpatterns = [
    path('', views.load_home),
    path('about-us/', views.about_us),
    path('login/login', views.login_user),
    path('register/', views.register_user),
    path('register/register', views.register_user),
    path('login/', views.login_user),
    path('logout/', views.logout),
]