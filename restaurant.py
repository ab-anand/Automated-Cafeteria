class Restaurant:
    def __init__(self, power, cost_menu):
        self.current_power = power
        self.max_power = power
        self.cost_menu = cost_menu

    def __del__(self):
        return

    def display_menu(self):
        """
        Displays the item along with its price
        """
        for item, price in self.cost_menu.items():
            print("+ {}: ${}".format(item.upper(), price))

    def order_cost(self, items):
        """
        This method takes a list of items/orders
        and check if it present in the MENU and
        returns its total price.
        :return: total_cost(int)
        """
        total_cost = 0
        try:
            for item in items:
                if item.lower() not in self.cost_menu:
                    # print("Failed")
                    total_cost = -1
                    raise KeyError(item)
                else:
                    total_cost += self.cost_menu[item.lower()]
        except KeyError as e:
            print("{} is not present in our menu. \n Kindly check the menu and try again.".format(item))

        return total_cost

    @property
    def get_power(self):
        return self.current_power

    def restore_power(self, incurred_cost):
        """
        :input: Takes the power/cost used by the order and restores it.
        """
        self.current_power = min(self.max_power, self.current_power + incurred_cost)

    def place_order(self, incurred_cost):
        """
        This method takes the amount of the order
        and checks if it has the power to process.
        :return: 1 if it has the power to process, 0 otherwise.
        """
        if incurred_cost > self.get_power:
            return 0
        else:
            self.current_power -= incurred_cost
            return 1
