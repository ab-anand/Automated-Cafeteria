import unittest
import sys

sys.path.insert(0, '..')

import data
from restaurant import Restaurant


class TestCafe(unittest.TestCase):

    def setUp(self):
        self.restaurant_A = Restaurant(data.power_A, data.items_price_restaurant_A)
        self.restaurant_B = Restaurant(data.power_B, data.items_price_restaurant_B)

    def test_get_power(self):
        result_1 = self.restaurant_A.get_power
        correct_answer_1 = data.power_A
        self.assertEqual(result_1, correct_answer_1)

        result_2 = self.restaurant_B.get_power
        correct_answer_2 = data.power_B
        self.assertEqual(result_2, correct_answer_2)

    def test_order_cost(self):
        order_list_1 = ["donuts", "Biryani", "coke"]
        result_1 = self.restaurant_A.order_cost(order_list_1)
        correct_answer_1 = 37
        self.assertEqual(result_1, correct_answer_1)

        result_2 = self.restaurant_B.order_cost(order_list_1)
        correct_answer_2 = 34
        self.assertEqual(result_2, correct_answer_2)

    def test_place_order(self):
        result_1 = self.restaurant_A.place_order(36)
        correct_answer_1 = 1

        result_2 = self.restaurant_B.place_order(52)
        correct_answer_2 = 0

        result_3 = self.restaurant_A.place_order(10)
        correct_answer_3 = 0

        self.assertEqual(result_1, correct_answer_1)
        self.assertEqual(result_2, correct_answer_2)
        self.assertEqual(result_3, correct_answer_3)

    def test_restore_power(self):
        x = self.restaurant_A.place_order(36)
        self.restaurant_A.restore_power(40)
        result_1 = self.restaurant_A.get_power
        correct_answer_1 = 36
        self.assertEqual(result_1, correct_answer_1)
