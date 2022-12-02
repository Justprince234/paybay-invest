from django.shortcuts import render
from rest_framework import generics
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

from .models import Tenor, Commodity, Dashboard, Bank, Withdraw, Crypto, WithdrawBank, Deposit, Items
from .serializers import TenorSerializer, CommoditySerializer, DashboardSerializer, BankSerializer, WithdrawSerializer, CryptoSerializer, WithdrawBankSerializer, DepositSerializer, ItemsSerializer

# Create your views here.
class TenorList(generics.ListCreateAPIView):
    queryset = Tenor.objects.all()
    serializer_class = TenorSerializer

class CommodityList(generics.ListCreateAPIView):
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def dashboard_api_view(request):
    
    if request.method == 'GET':
        items = Dashboard.objects.filter(owner=request.user,)
        serializer = DashboardSerializer(items, many=True)
        return JsonResponse(serializer.data, safe =False)
    
    elif request.method == 'POST':
        owner = request.user
        data = JSONParser().parse(request)
        serializer =DashboardSerializer(data = data)
 
        if serializer.is_valid():
            serializer.save(owner)
            return JsonResponse(serializer.data,status =201)
        return JsonResponse(serializer.errors,status = 400)

class BankList(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class ItemsList(generics.ListCreateAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

class WithdrawAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = WithdrawSerializer

    def get(self, request, *args, **kwargs):
        user = self.context['request'].user
        items = Withdraw.objects.filter(owner=user,)
        serializer = WithdrawSerializer(items,context={'request':request}, many=True)
        return JsonResponse(serializer.data, safe =False)

    def post(self, request, *args, **kwargs):
        profile_value =Dashboard.objects.get(owner=user,).profile_value
        dashboard = Dashboard.objects.filter(owner=user,)
        serializer = WithdrawSerializer(data=request.data, context={'request':request}) 
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user.save()

            profile_value -= serializer.validated_data['amount']
            dashboard.update(profile_value=profile_value)

        return Response({
            "status": "Transaction successful",
            "user": WithdrawSerializer(serializer.validated_data).data
            })

class CryptoList(generics.ListCreateAPIView):
    queryset = Crypto.objects.all()
    serializer_class = CryptoSerializer

class WithdrawBankList(generics.ListCreateAPIView):
    queryset = WithdrawBank.objects.all()
    serializer_class = WithdrawBankSerializer

class DepositList(generics.ListCreateAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer
