"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase

class HomepageUrlTest(TestCase):
    def test_success_when_get_homepage(self):
        response = self.client.get('/')        
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'index.html')

__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

