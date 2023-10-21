import random

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
    "water": random.randint(300, 800),
    "milk": random.randint(300, 800),
    "coffee": random.randint(300, 800),
    "money": random.randint(5, 10),
}


def check_resources(order):

    for ingredient in MENU[order]["ingredients"]:
        if MENU[order]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
        else:
            return True


def process_coins():
    quarters_value = 0.25
    dimes_value = 0.10
    nickles_value = 0.05
    pennies_value = 0.01

    users_quarters = int(input("Please Insert Coins:\nQuarters: "))
    users_dimes = int(input("Please Insert Coins:\nDimes: "))
    user_nickles = int(input("Please Insert Coins:\nNickles: "))
    user_pennies = int(input("Please Insert Coins:\nPennies: "))

    users_quarters *= quarters_value
    users_dimes *= dimes_value
    user_nickles *= nickles_value
    user_pennies *= pennies_value

    total_user_money = user_nickles + user_pennies + users_dimes + users_quarters

    return total_user_money


def check_transaction_successful(order, money):
    if MENU[order]["cost"] > money:
        print("Sorry that's not enough money. Money refunded.")
    elif MENU[order]["cost"] < money:
        resources["money"] += MENU[order]["cost"]
        money -= MENU[order]["cost"]
        print(f"Here is ${round(money, 2)} dollars in change.")


def make_coffe(order):

    for ingredient in MENU[order]["ingredients"]:
        resources[ingredient] -= MENU[order]["ingredients"][ingredient]
    print(f"Here is your {order}. Enjoy!")


order = ""

while order != "off":

    order = input("What would you like? (espresso/latte/cappuccino):")

    while order != "espresso" and order != "latte" and order != "cappuccino" and order != "off" and order != "report":
        order = input("Please select a valid option\nWhat would you like? (espresso/latte/cappuccino):")

    if order == "report":
        print(f"Water: {resources["water"]}\nMilk: {resources["milk"]}\nCoffe: {resources["coffee"]}\nMoney: {resources["money"]}$")

    if order == "cappuccino" or order == "espresso" or order == "latte":

        available_resources = check_resources(order)
        if available_resources is True:
            user_money = process_coins()
            check_transaction_successful(order, user_money)
            make_coffe(order)
