# tests/test_inventory.py

import unittest
from app import Inventory

class TestInventory(unittest.TestCase):
    def test_add_and_get_items(self):
        inv = Inventory()
        inv.add_item("Shoes")
        inv.add_item("Socks")
        self.assertEqual(inv.get_items(), ["Shoes", "Socks"])

if __name__ == '__main__':
    unittest.main()
