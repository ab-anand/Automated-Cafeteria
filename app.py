from cafe import Cafeteria

item1 = ["coke", "biryani"]
item2 = ["donuts", "sdfd", "soup", "biryani"]
item3 = ["donuts", "soup"]
item4 = ["coke", "biryani", "coke", "biryani", "coke", "biryani", "coke", "biryani"]
item5 = []
cafe1 = Cafeteria()
# cafe2 = Cafeteria()

cafe1.display_complete_menu()

cafe1.check_best_price_for_order(item1)
cafe1.place_order(item1)
cafe1.place_order(item3)
cafe1.place_order(item2)
cafe1.place_order(item4)
cafe1.place_order(item5)
