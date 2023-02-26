from account.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(email='admin@paybay-invest.com').exists():
            User.objects.create_superuser(
                email='admin@paybay-invest.com',
                password='America234'
            )
        print('Superuser has been created.')