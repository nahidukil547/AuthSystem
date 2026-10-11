from django.urls import path
from . import views
from rest_framework.authtoken import views as TokenViews
urlpatterns = [
    path('', views.TestResponse, name='Test Response'),
    path('login/', TokenViews.obtain_auth_token)
]
