import unittest
from datetime import datetime
from category.domain.entities import Category
class TestCategory(unittest.TestCase):
    def test_constructor(self):
        category = Category('neymar','melhor do mundo',True,datetime.now())
        self.assertEqual(category.name , 'neymar')
        self.assertEqual(category.description , 'melhor do mundo')
        self.assertEqual(category.is_active , True)
        self.assertIsInstance(category.created_at , datetime)