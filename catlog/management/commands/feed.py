#!/usr/local/bin/python3

from django.core.management.base import BaseCommand

from .Database.dbRessources import connect
from .Utils.datafeed import feed_application


class Command(BaseCommand):
    help = 'Feeding database from Openfoodfacts'

    def handle(self, *args, **options):
        # Access to database to access to the data
        print("Starting feed")
        connection = connect()
        feed_application(connection)
        print('feed done')
