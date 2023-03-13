"""
Sample Test
"""
from django.test import SimpleTestCase

from app import calc


class ClacTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers Together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test Subtracting Number"""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)
