MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def machine_run():
    while True:
        coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if coffee_choice == "off":
            print("Shutting down")
            return
        elif coffee_choice == "report":
            print(f"{get_resource()}")
        else:
            if not check_resource(coffee_choice):
                print("No enough resources")
            else:
                money = collect_coin()
                if not check_money(money, coffee_choice):
                    print("Money not enough ")
                else:
                    make_coffee(money, coffee_choice)


# TODO 1: CHECK MONEY
def check_money(money, coffee_choice):
    return money - MENU[coffee_choice]["cost"] > 0


# TODO 2: MAKE COFFEE (1. RECALCULATE RESOURCE, 2. ADD MONEY 3.PRINT COFFEE)
def make_coffee(money, coffee_choice):
    """These codes are not good enough. need to try for item in to simplify"""

    print(f'Return {money - MENU[coffee_choice]["cost"]}')
    resources["money"] += MENU[coffee_choice]["cost"]
    resources["water"] -= MENU[coffee_choice]["ingredients"]["water"]
    resources["milk"] -= MENU[coffee_choice]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee_choice]["ingredients"]["coffee"]
    print(f"Please enjoy {coffee_choice}")


# TODO 3: CHECK RESOURCE
def get_resource():
    return f'Water {resources["water"]}\nMilk {resources["milk"]}\n' \
           f'Coffee {resources["coffee"]}\nMoney {resources["money"]}'


def check_resource(coffee_choice):
    """These codes are not good enough. need to try for item in to simplify"""

    water = resources["water"] - MENU[coffee_choice]["ingredients"]["water"]
    milk = resources["milk"] - MENU[coffee_choice]["ingredients"]["milk"]
    coffee = resources["coffee"] - MENU[coffee_choice]["ingredients"]["coffee"]
    if water < 0 or milk < 0 or coffee < 0:
        return False
    else:
        return True


# TODO 4: COLLECT COIN
def collect_coin():
    quarter = int(input("How many quarters "))
    dime = int(input("How many dimes "))
    nickle = int(input("How many nickles "))
    penny = int(input("How many pennies "))
    return 0.25 * quarter + 0.1 * dime + 0.05 * nickle + 0.01 * penny


machine_run()
