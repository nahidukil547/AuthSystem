from django.urls import path
from . import views
from rest_framework.authtoken import views as TokenViews
urlpatterns = [
    path('', views.TestResponse, name='Test Response'),
    path('login/', TokenViews.obtain_auth_token),
    path('custome/login/', views.CustomeLoginView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('custome/register', views.custome_register),
    path('change_password/', views.change_Password),
]
