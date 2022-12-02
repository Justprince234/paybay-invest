from django.urls import path
from knox import views as knox_views
from account import views
from account.views import ContactList
from core.views import DepositList, TenorList, CommodityList, dashboard_api_view, BankList, withdraw_api_view, CryptoList, WithdrawBankList, ItemsList

urlpatterns = [
    path('register/', views.RegisterAPI.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('contact/', views.ContactList.as_view(), name='contact'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('user/', views.UserAPI.as_view(), name='user'),
    path('tenor/', TenorList.as_view()),
    path('commodity/', CommodityList.as_view()),
    path('dashboard/', dashboard_api_view),
    path('bank/', BankList.as_view()),
    path('items/', ItemsList.as_view()),
    path('withdraw/', withdraw_api_view),
    path('crypto/', CryptoList.as_view()),
    path('withdrawbank/', WithdrawBankList.as_view()),
    path('deposit/', DepositList.as_view()),
    path('contact/', ContactList.as_view())
]