"""
Django commands to wait for db to be available
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError


from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database"""

    def handle(self, *args, **kwargs):
        """Entry point for command"""

        # Display a message indicating that the script is waiting for the db
        self.stdout.write('Waiting for the database...')
        # Initialize a variable to track the database status
        db_up = False
        # Continue looping until the database is available
        while db_up is False:
            try:
                # Attempt to check the database connection
                self.check(databases=['default'])
                # If successful, set the database status to up
                db_up = True
            except (Psycopg2OpError, OperationalError):
                # If there's an error, display a message and wait for 1 second
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        # Display a success message when the database is available
        self.stdout.write(self.style.SUCCESS('Database is available'))
