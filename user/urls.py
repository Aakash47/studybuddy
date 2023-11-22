from django.urls import path
from user import views as user_view

urlpatterns = [
    path('', user_view.home, name="home"),
    path('register/', user_view.registeruser, name="register"),
    path('login/', user_view.loginuser, name="login"),
    path('logout/', user_view.logoutuser, name="logout"),
]