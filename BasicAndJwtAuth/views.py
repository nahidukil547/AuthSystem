from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpRequest 
from .forms import RegisterForm
from .serializer import RegisterSerializer
from django.contrib.auth.models import User
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





class RegisterView(ObtainAuthToken):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
   
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