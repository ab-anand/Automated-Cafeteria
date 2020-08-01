import sys
import data

from restaurant import Restaurant


class Cafeteria:
    def __init__(self):
        self.item_costs_A = data.items_price_restaurant_A
        self.power_A = data.power_A
        self.restaurant_A = Restaurant(self.power_A, self.item_costs_A)

        self.item_costs_B = data.items_price_restaurant_B
        self.power_B = data.power_B
        self.restaurant_B = Restaurant(self.power_B, self.item_costs_B)

        self.item_costs_C = data.items_price_restaurant_C
        self.power_C = data.power_C
        self.restaurant_C = Restaurant(self.power_C, self.item_costs_C)

        self.restaurants = {"A": self.restaurant_A, "B": self.restaurant_B, "C": self.restaurant_C}

    def __del__(self):
        return

    def display_complete_menu(self):
        """
        This method displays the MENU of all the present restaurant
        """
        print("")
        for restaurant_name, restaurant in self.restaurants.items():
            print("MENU FOR RESTAURANT: {}".format(restaurant_name))
            restaurant.display_menu()
            print("")

    def check_best_price_for_order(self, orders):
        """
        This method finds the best price and availability for any given list of orders
        input: Takes list of orders as input
        returns: tuple of least_order_cost(int), restaurant name(string)
        """

        if len(orders) == 0:
            print("No items found. Please place some items in your order.")
            return -1, None

        orders = [order.lower() for order in orders]
        least_order_cost = sys.maxsize
        cheapest_restaurant = None

        for restaurant_name, restaurant in self.restaurants.items():
            cost = restaurant.order_cost(orders)
            restaurant_power = restaurant.get_power
            if cost == -1:
                least_order_cost = -1
                break
            if least_order_cost > cost and restaurant_power >= cost:
                least_order_cost = cost
                cheapest_restaurant = restaurant_name

        if least_order_cost == -1:
            return -1, None
        elif cheapest_restaurant is None:
            print("Can't place order! Restaurants busy, please visit in sometime.")
            return -1, None
        else:
            print("Order Cost: ${} \n Cheapest Restaurant: Restaurant {}".format(least_order_cost, cheapest_restaurant))
            return least_order_cost, cheapest_restaurant

    def place_order(self, orders):
        """
        This method uses the above check_best_price_for_order() method
        to check the best price and availability of an order and finally
        places the order.
        Once the order is placed and completed the power is restored using
        restore_power()
        :input: takes list of orders
        :returns: returns 1 if order can be placed successfully else 0
        """
        least_order_cost, cheapest_restaurant = self.check_best_price_for_order(orders)
        if least_order_cost != -1:
            self.restaurants[cheapest_restaurant].place_order(least_order_cost)
            self.restaurants[cheapest_restaurant].restore_power(least_order_cost)
            print("Your order has been placed successfully!")
            return 1
        else:
            print("Error placing the order!")
            return 0
