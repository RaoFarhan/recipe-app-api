"""
Sample Test
"""
from  django.test import SimpleTestCase

from app import calc


class ClacTests():
    """Test the calc module"""

    
    def test_add_numbers(self):
        """Test adding numbers Together"""
        res = calc.add(5,6)

        self.assertequal(res, 11)
