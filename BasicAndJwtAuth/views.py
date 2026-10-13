from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpRequest 
from .forms import RegisterForm
from .serializer import RegisterSerializer, ChangePasswordSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
# Create your views here.
def TestResponse(requst):
    
    return HttpResponse('Hello This is for testing')

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def user_register(request):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    return Response(content)

class CustomeLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context= {'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        token, create = Token.objects.get_or_create(user=user)

        user.save()

        return Response({
            'token':token.key,
            'user_id':user.pk,
            'message':'Welcome, Status 200 Ok'
        })





class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes =[]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, create = Token.objects.get_or_create(user=user)
            user.save()

            return Response({
                'token':token.key,
                "user": {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email
                    },
                'message':'Welcome, Status 200 Ok'
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

@api_view(['post'])
@permission_classes([])
def custome_register(request):
    # queryset= User.objects.all()
    # print('first hello')
    if request.method =="POST":
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, create = Token.objects.get_or_create(user=user)
            return Response({
                            'token':token.key,
                            "user": {
                                    "id": user.id,
                                    "username": user.username,
                                    "email": user.email
                                },
                            'message':'Welcome, Status 200 Ok'
                        })
        return Response({
            'errors': serializer.errors,
            'message': 'Validation failed'
        }, status=status.HTTP_400_BAD_REQUEST)
    return Response({
        'error': 'Only POST method allowed'
    }, status=status.HTTP_405_METHOD_NOT_ALLOWED)

from django.contrib.auth import authenticate
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_Password(request):
    if request.method == "POST":
        username = request.data.get('username')
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')
        print(request.data)
       
        user = request.user
        
        if username != user.username:
            return Response(
                {'error': 'Username does not match the authenticated user.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if new_password != confirm_password:
            return Response(
                {'error': 'New password and confirm password do not match.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )  
        user.set_password(new_password)
        user.save()

        token,create = Token.objects.get_or_create(user=user)

        return Response(
            {
                'Token':token.key,
                'User':{
                    'User_id':user.pk,
                    'Username':user.username,
                    'email':user.email,
                },
                'message':'Welcome, Status 200 Ok'
            }
        )

    return Response({
        'error': 'Only POST method allowed'
    }, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    