from cafe import Cafeteria

item1 = ["coke", "biryani"]
# case with item not present
item2 = ["donuts", "sdfd", "soup", "biryani"]
item3 = ["donuts", "soup"]
# case with total cost exceeding restaurants power
item4 = ["coke", "biryani", "coke", "biryani", "coke", "biryani", "coke", "biryani"]
# case with empty item
item5 = []
# case with passing orders as string and tuple
item6 = "coke biryani"
item8 = "waffles", "donuts"
# case with ambiguous values
item7 = 12
item9 = None

cafe1 = Cafeteria()
# cafe2 = Cafeteria()

cafe1.display_complete_menu()
cafe1.check_best_price_for_order(item1)
cafe1.place_order(item1)
cafe1.place_order(item3)
cafe1.place_order(item2)
cafe1.place_order(item4)
cafe1.place_order(item5)
cafe1.place_order(item6)
cafe1.place_order(item7)
cafe1.place_order(item8)
cafe1.place_order(item9)
