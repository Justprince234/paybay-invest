from django.contrib import admin
from .models import Tenor, Commodity, Dashboard, Bank, Withdraw, Crypto, WithdrawBank, Deposit, Items

# Register your models here.
admin.site.register(WithdrawBank)
admin.site.register(Bank)
admin.site.register(Crypto)
admin.site.register(Withdraw)
admin.site.register(Tenor)
admin.site.register(Commodity)
admin.site.register(Dashboard)
admin.site.register(Deposit)
admin.site.register(Items)
