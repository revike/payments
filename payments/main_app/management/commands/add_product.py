from django.core.management import BaseCommand

from main_app.models import Item


class Command(BaseCommand):
    """Команда для создания супер юзера"""

    def handle(self, *args, **options):
        if Item.objects.all().count() == 0:
            Item.objects.create(name='product', description='desc', price=40)
