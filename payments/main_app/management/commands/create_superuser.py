from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Команда для создания супер юзера"""

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin'):
            User.objects.create_superuser(
                username='admin', password='admin',
            )
