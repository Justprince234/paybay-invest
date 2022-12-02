from django.db.models.base import Model
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from knox.auth import TokenAuthentication
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, ContactSerializer
from rest_framework.permissions import IsAuthenticated
from .models import User, Contact
from rest_framework import permissions
from django.conf import settings
from django.contrib.auth import login
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import serializers

from django.shortcuts import render,HttpResponseRedirect,Http404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required

from django.contrib.sites.shortcuts import get_current_site

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # Confirmation Email Configuration
        current_site = get_current_site(request)

        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1],
        'domain': current_site.domain
        })


# Login API
class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })
        
# Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# @api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
# def profiles_api_view(request):
    
#     if request.method == 'GET':
#         items = UpdateUser.objects.filter(owner=request.user,)
#         serializer = UpdateUserSerializer(items, many=True)
#         return JsonResponse(serializer.data, safe =False)
    
#     elif request.method == 'POST':
#         owner = request.user
#         data = JSONParser().parse(request)
#         serializer =UpdateUserSerializer(data = data)
 
#         if serializer.is_valid():
#             serializer.save(owner)
#             return JsonResponse(serializer.data,status = 201)
#         return JsonResponse(serializer.errors,status = 400)
 

@api_view(['GET'])
def all_user_view(request):
    
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe =False)

 