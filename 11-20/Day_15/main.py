MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 600,
    "milk": 500,
    "coffee": 300,
}

should_continue = True
profit = 0


def check_resources(ingredients):
    """Returns True when are enough ingredients, otherwise returns False"""
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


def coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def successful_transaction(given_money, drink_cost):
    """Returns True when the payment is accepted, otherwise returns False"""
    if given_money >= drink_cost:
        change = round(given_money - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, ingredients):
    """Deduct the required ingredients from the resources."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name} ☕")


while should_continue:
    answer = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if answer == "off":
        should_continue = False
    elif answer == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[answer]
        if check_resources(drink["ingredients"]):
            payment = coins()
            if successful_transaction(payment, drink["cost"]):
                make_coffee(answer, drink["ingredients"])
