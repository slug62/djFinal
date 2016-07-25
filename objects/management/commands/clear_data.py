__author__ = 'faculty'

from objects.models import Parent, Shape, Child, Length


from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "clear sample from database"

    def handle(self, *args, **options):
        Shape.objects.all().delete()

