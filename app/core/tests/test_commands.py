"""
Test custom Django management commands
"""

from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


# Patch the 'check' method of the custom management command for testing
@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Tests commands."""

    # Test case for the scenario when the database is ready
    def test_wait_for_db_ready(self, patched_check):
        """Tests waiting for the db if db ready"""

        # Set the return value of the patched 'check' method to True
        patched_check.return_value = True
        # Call the 'wait_for_db' command
        call_command("wait_for_db")
        # Assert that the 'check' method was called with the correct arguments
        patched_check.assert_called_once_with(databases=['default'])

    # Test case for the scenario when there is a delay in waiting for the db
    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for database when getting OperationalError"""

        # Set up the side effects for the patched 'check' method
        patched_check.side_effect = [Psycopg2Error] * 2 + \
                                    [OperationalError] * 3 + [True]
        # Call the 'wait_for_db' command
        call_command('wait_for_db')

        # Assert the number of calls to the 'check' method and the
        # arguments used
        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
