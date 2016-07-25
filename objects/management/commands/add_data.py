__author__ = 'faculty'


from django.core.management.base import BaseCommand
from objects.models import Shape


class Command(BaseCommand):
    help = "populate database with sample data"

    def handle(self, *args, **options):
        s1 = Shape(name='box', description='rectangle oriented along the axes')
        s1.save()
        s2 = Shape(name='star', description='five pointed star')
        s2.save()
        s3 = Shape(name='blob', description='amorphous, somewhat like a cloud')
        s3.save()
