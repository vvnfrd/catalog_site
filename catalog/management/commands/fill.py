from django.core.management import BaseCommand
from catalog.models import Category, Product
class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category_list = [
            {'name': 'producti', 'description': 'a'},
            {'name': 'himiya', 'description': 'b'},
            {'name': 'tehnika', 'description': 'c'},
            {'name': 'uslugi', 'description': 'd'}
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )
        Category.objects.bulk_create(category_for_create)

        product_list = [
            {'name': 'yabloki', 'description': 'a', 'category': Category.objects.get(name = 'producti'), 'price': 10},
            {'name': 'soda', 'description': 'b', 'category': Category.objects.get(name = 'himiya'), 'price': 10},
            {'name': 'telefon', 'description': 'c', 'category': Category.objects.get(name ='tehnika'), 'price': 10},
            {'name': 'clining', 'description': 'd', 'category': Category.objects.get(name ='uslugi'), 'price': 10}
        ]

        product_for_create = []
        for product_item in product_list:
            product_for_create.append(
                Product(**product_item)
            )
        Product.objects.bulk_create(product_for_create)