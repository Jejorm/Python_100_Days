from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()

while True:

    options = menu.get_items()
    user_option = input(f"What would you like? ({options}): ")

    if user_option == "off":
        break

    elif user_option == "report".lower():
        coffee_maker.report()
        money.report()

    else:
        coffee = menu.find_drink(user_option)

        if coffee_maker.is_resource_sufficient(coffee) and money.make_payment(coffee.cost):
            coffee_maker.make_coffee(coffee)

        else:
            break

