from django.urls import path
#from .views import UserRegisterView
from . import views

urlpatterns = [
    path('register/', views.register_view, name="register"),
    #path('login/', views.login_view, name="login"),
]