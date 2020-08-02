# Cafeteria App

An automated cafeteria system that allows any customer to place order from the 
available restaurants without human intervention. Users can get the order from the
restaurant which provides it in the minimum value. 
<br> Users can check the menu from all the restaurants. Restaurants are initiated with
a particular power and menu. Whenever a user places an 
order from the Cafeteria, the best price for that order is checked depending on the 
power availability of the restaurant. Once the order is placed the total power of the 
restaurant is reduced and once the order is delivered successfully the power 
is restored back to the restaurant.

## Environment
* version: 1.0
* support: UNIX with Python 2.x, 3.x 

### Getting Started
Project structure

```
cafeteria/
    ├── app.py
    ├── bin
    │   ├── setup
    │   └── setup.sh
    ├── cafe.py
    ├── data.py
    ├── README.md
    ├── restaurant.py
    ├── test_main.py
    └── tests
        ├── test_cafe.py
        └── test_restaurant.py

```

* `bin` directory has executables to setup and run the project.
*  `tests` directory has unit tests for all the methods in the models, it is controlled 
by `test_main.py` file in the `cafeteria` directory
* `restaurant.py` holds the implementation of Restaurant class.
* `cafe.py` holds the implementation of Cafeteria class.
* `Cafeteria` holds [has_a](https://en.wikipedia.org/wiki/Has-a) relationship with `Restaurant` class. 
Thus a `Composite` relationship logic has been used while designing them. 
* `test_main.py` runs all the unit tests written in the `tests` directory.

### Installing
Once u have cloned/uncompressed project in your directory say cafeteria, change to the project directory
via terminal and run the setup

```
$ cd cafeteria
```

Run setup file
```
$ bin/setup
```
This will do the necessary setup and run all the unittests.

On successful installation you should see messages similar to below:

```
Building Cafeteria app version 1.0
Reading package lists... Done
Building dependency tree       
Reading state information... Done
python3 is already the newest version (3.6.7-1~18.04).
python3-pip is already the newest version (9.0.1-2.3~ubuntu1.18.04.1).
0 upgraded, 0 newly installed, 0 to remove and 18 not upgraded.
--- Running automated tests for Cafeteria app ---
....Order Cost: $33 
 Cheapest Restaurant: Restaurant C
soda is not present in our menu. 
 Kindly check the menu and try again.
No items found. Please place some items in your order.
.Order Cost: $33 
 Cheapest Restaurant: Restaurant C
Your order has been placed successfully!
soda is not present in our menu. 
 Kindly check the menu and try again.
Error placing the order!
.
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
Setup done Successfully!

```

**NOTE**- If you're running a `WINDOWS` machine, then just install `Python` and then open the `app.py` to run 
you're own test cases(shown below).  
### Usage

* The `app.py` file has been created to play around. It has most of the examples 
and usage covered but let's get through some of the important methods.

* To run your own test cases, you can add more cases in `app.py` itself or can create another python file 
in the same directory. 

* As shown in `app.py` once the `Cafeteria` object is created the menu can be checked as:
```
>> cafe1 = Cafeteria()
>> cafe1.display_complete_menu()

Output:

MENU FOR RESTAURANT: A
+ WAFFLES: $9
+ DONUTS: $10
+ PASTRY: $8
+ SOUP: $6
+ BIRYANI: $22
+ COKE: $5

MENU FOR RESTAURANT: B
+ WAFFLES: $10
+ DONUTS: $11
+ PASTRY: $9
+ SOUP: $7
+ BIRYANI: $20
+ COKE: $3

MENU FOR RESTAURANT: C
+ WAFFLES: $12
+ DONUTS: $9
+ PASTRY: $10
+ SOUP: $10
+ BIRYANI: $18
+ COKE: $6

```

* Checking the best(lowest) price for that order
```
>> cafe1.check_best_price_for_order(["coke", "biryani"])

Output: 

Order Cost: $23 
Cheapest Restaurant: Restaurant B
```

* Placing the order
```
>> cafe1.place_order(["coke", "biryani"])

Output:

******* Placing your order. Please wait! ********
Order Cost: $23 
Cheapest Restaurant: Restaurant B
Your order has been placed successfully!
```

* You can also pass the order as `string`
```
>> cafe1.place_order("coke biryani")

Output:

******* Placing your order. Please wait! ********
Order Cost: $23
Cheapest Restaurant: Restaurant B
Your order has been placed successfully! 

```

* You can also pass the order as `tuple`
```
>> cafe1.place_order("waffles", "donuts")

Output:

******* Placing your order. Please wait! ********
Order Cost: $19
Cheapest Restaurant: Restaurant A
Your order has been placed successfully! 
```

* Placing an order which is not in the menu
```
>> cafe1.place_order(["donuts", "sdfd", "soup", "biryani"])

Output:

******* Placing your order. Please wait! ********
sdfd is not present in our menu. 
Kindly check the menu and try again.
Error placing the order!
```

* Placing an empty order
```
>> cafe1.place_order([])

Output:

******* Placing your order. Please wait! ********
No items found. Please place some items in your order.
Error placing the order!
```

* Placing order with value more than a restaurant's power
```
>> cafe1.place_order(["coke", "biryani", "coke", "biryani", "coke", "biryani", "coke", "biryani"])

Output:

******* Placing your order. Please wait! ********
Can't place order! Restaurants busy, please visit in sometime.
Error placing the order!
```

* Placing an order with ambiguous data types
```
>> cafe1.place_order(12)

Output:

******* Placing your order. Please wait! ********
Error placing the order!
```

**NOTE**- These commands should be executed in a python file with `Cafeteria` object 
initialized. As shown in `app.py` file.

### Extras

* running the tests. In your terminal type
```
$ python test_main.py
```

* adding more restaurants/power/items: make changes in the `data.py` file. In case you 
are adding restaurants, do the necessary changes in `__init__` method of `cafe.py` file.
Given example for change in
`cafe.py` after adding a restaurant(let's say D).
```
def __init__(self):
    .    
    .
    .

    self.item_costs_D = data.items_price_restaurant_D
    self.power_D = data.power_D
    self.restaurant_D = Restaurant(self.power_D, self.item_costs_D)

    self.restaurants = {"A": self.restaurant_A, "B": self.restaurant_B,
                         "C": self.restaurant_C, "D": self.restaurant_D}
```

* currently the power consumption(while placing an order) and restoring the power(once order is successfully completed)
goes together(check `place_order` method in `cafe.py`) because there wasn't any requirement specified in the problem statement 
but any logic to lapse the time in between can be added. For example one can
add a timestamp with each order and after that timestamp only the power would be restored. 

### Code Time Complexity
Assuming there are M restaurants in the cafeteria with each having N items. 
And the items in an order placed by the user is Z. 
Big O Complexity for various operations are given.

* *display_complete_menu()*: O(M*N) Time

* *check_best_price_for_order()*: O(M*Z) (for each restaurant calculates the price using the dictionary)

* *place_order()*: O(M*Z) 

### Author
* **Ayushi Rastogi** - [ayushi-24git](https://github.com/ayushi-24git)