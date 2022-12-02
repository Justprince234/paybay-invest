from rest_framework import serializers
from .models import Tenor, Commodity, Dashboard, Bank, Withdraw, Crypto, WithdrawBank, Deposit, Items
from rest_framework.fields import CurrentUserDefault


class TenorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenor
        fields = '__all__'

class CommoditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commodity
        fields = '__all__'

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'

class DashboardSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Dashboard
        fields = '__all__'

    def save(self, **kwargs):
        """Include default for read_only `account` field"""
        kwargs["owner"] = self.fields["owner"].get_default()
        return super().save(**kwargs)

class WithdrawSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    dashboard = DashboardSerializer(many=True)
    class Meta:
        model = Withdraw
        fields = '__all__'

    def save(self, **kwargs):
        """Include default for read_only `account` field"""
        kwargs["owner"] = self.fields["owner"].get_default()
        return super().save(**kwargs)

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        fields = '__all__'

class WithdrawBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = WithdrawBank
        fields = '__all__'

class DepositSerializer(serializers.ModelSerializer):
    bank = WithdrawBankSerializer(many=True)
    crypto = CryptoSerializer(many=True)
    class Meta:
        model = Deposit
        fields = '__all__'