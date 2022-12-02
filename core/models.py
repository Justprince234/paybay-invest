from django.db import models
from django.conf import settings
from datetime import datetime
from django.utils import timezone
from datetime import timedelta


STATUS = (
    ('Pending','Pending'),
    ('Sent','Sent')
)

# Create your models here.
class Tenor(models.Model):
    name = models.CharField(max_length=50)
    days = models.CharField(max_length=50)
    percentage = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Investment Tenor"

    def __str__(self):
        return self.name

class Commodity(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=50,decimal_places=2) 
    expected_return = models.DecimalField(max_digits=50,decimal_places=2)
    percentage = models.DecimalField(max_digits=50,decimal_places=2) 
    date = datetime.now()

    class Meta:
        verbose_name_plural = "Investment Stages"

    def __str__(self):
        return self.name

class Dashboard(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='dashboards', on_delete=models.CASCADE)
    profile_value = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    class Meta:
        verbose_name_plural = "User Dashboard"

    def __str__(self):
        return str(self.owner)

class Withdraw(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='withdraw', on_delete=models.CASCADE)
    dashboard = models.ForeignKey(Dashboard, related_name='dashboard', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    account  = models.IntegerField()
    amount = models.IntegerField()
    swift = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=50)
    bank_address = models.CharField(max_length=50)
    bank_state = models.CharField(max_length=50)
    bank_zip_code = models.CharField(max_length=50)
    bank_country = models.CharField(max_length=50)
    additional_instructions = models.TextField()
    status = models.CharField(choices=STATUS, default="Pending", max_length=9)

    class Meta:
        verbose_name_plural = "Client Withdrawal Details"

    def __str__(self):
        return str(self.owner)

class Bank(models.Model):
    name = models.CharField(max_length=100)
    account  = models.IntegerField()
    swift = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=50)
    bank_address = models.CharField(max_length=50)
    bank_state = models.CharField(max_length=50)
    bank_zip_code = models.CharField(max_length=50)
    bank_country = models.CharField(max_length=50)
    additional_instructions = models.TextField()

    class Meta:
        verbose_name_plural = "Client Withdrawal Bank Details"

    def __str__(self):
        return self.name

class Crypto(models.Model):
    wallet_name = models.CharField(max_length=50)
    wallet_address = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "My crypto Wallet addresses"

    def __str__(self):
        return self.wallet_name

class WithdrawBank(models.Model):
    name = models.CharField(max_length=100)
    account  = models.IntegerField()
    swift = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=50)
    bank_address = models.CharField(max_length=50)
    bank_state = models.CharField(max_length=50)
    bank_zip_code = models.CharField(max_length=50)
    bank_country = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "My Bank Details"

    def __str__(self):
        return self.name

class Deposit(models.Model):
    bank = models.ForeignKey(WithdrawBank, related_name='depositbank', on_delete=models.CASCADE)
    crypto = models.ForeignKey(Crypto, related_name='cryptos', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Deposit Bank and Crypto Details"

    def __str__(self):
        return self.bank.name

def return_date_time():
    now = timezone.now()
    return now + timedelta(days=1)

class Items(models.Model):
    value = models.CharField(max_length=50)
    date = models.DateField(default=return_date_time)

    class Meta:
        verbose_name_plural = "Not Needed"