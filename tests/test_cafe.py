import unittest
import sys

from cafe import Cafeteria

sys.path.insert(0, '')


class TestCafe(unittest.TestCase):

    def setUp(self):
        self.cafe1 = Cafeteria()
        self.order_list_1 = ["donuts", "Biryani", "coke"]
        self.order_list_2 = ["soda", "biryani"]
        self.order_list_3 = []

    def test_check_best_price_for_order(self):
        result_1 = self.cafe1.check_best_price_for_order(self.order_list_1)
        correct_answer_1 = (32, "C")
        self.assertEqual(result_1, correct_answer_1)

        result_2 = self.cafe1.check_best_price_for_order(self.order_list_2)
        correct_answer_2 = (-1, None)
        self.assertEqual(result_2, correct_answer_2)

        result_3 = self.cafe1.check_best_price_for_order(self.order_list_3)
        correct_answer_3 = (-1, None)
        self.assertEqual(result_3, correct_answer_3)

    def test_place_order(self):
        result_1 = self.cafe1.place_order(self.order_list_1)
        correct_answer_1 = 1
        self.assertEqual(result_1, correct_answer_1)

        result_2 = self.cafe1.place_order(self.order_list_2)
        correct_answer_2 = 0
        self.assertEqual(result_2, correct_answer_2)


if __name__ == '__main__':
    unittest.main()
