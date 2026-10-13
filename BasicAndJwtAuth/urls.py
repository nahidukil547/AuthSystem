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


"""

{
    "first_name":"Jon",
    "last_name":"doe",
    "email":"jon@gmail.com",
    "username":"jon",
    "password":"123",
    "confirm_password":"123"
}


{
    "token": "f08058267a9a7015cd889787cc7155b9801ab7ff",
    "user": {
        "id": 5,
        "username": "jon",
        "email": "jon@gmail.com"
    },
    "message": "Welcome, Status 200 Ok"
}

"""