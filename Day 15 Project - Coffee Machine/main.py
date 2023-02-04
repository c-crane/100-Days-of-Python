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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


keep_going = True
water = 300
milk = 200
coffee = 100
money = 0


def price_drink():
    tot_quarters = quarters * 0.25
    tot_dimes = dimes * 0.1
    tot_nick = nickels * 0.05
    tot_pen = pennies * 0.01
    total = round(tot_quarters + tot_dimes + tot_nick + tot_pen, 2)
    # print(total)
    if total > price_of_drink:
        change = round(total - price_of_drink, 2)
        print(f"Your change is: ${change}")
        print(f"Here is your {customer} ☕️. Enjoy!")
    else:
        print("Not enough money")
    return total


while keep_going:

    customer = input("What would you like? (espresso/latte/cappuccino): ")
    if customer != "report" and customer != "off":
        if water < int(MENU[customer]['ingredients']['water']):
            print("Sorry, we are out of water.")
            break
        elif customer != "espresso" and milk < int(MENU[customer]['ingredients']['milk']):
            print("Sorry, we are out of milk.")
            break
        elif coffee < int(MENU[customer]['ingredients']['coffee']):
            print("Sorry we are out of coffee.")
            break

    if customer == "espresso":
        water -= MENU['espresso']['ingredients']['water']
        coffee -= MENU['espresso']['ingredients']['coffee']
        money += MENU[customer]['cost']
    elif customer == "latte":
        water -= MENU['latte']['ingredients']['water']
        milk -= MENU['latte']['ingredients']['milk']
        coffee -= MENU['latte']['ingredients']['coffee']
        money += MENU[customer]['cost']
    elif customer == "cappuccino":
        water -= MENU['cappuccino']['ingredients']['water']
        milk -= MENU['cappuccino']['ingredients']['milk']
        coffee -= MENU['cappuccino']['ingredients']['coffee']
        money += MENU[customer]['cost']
    elif customer == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${money}")
    elif customer == "off":
        keep_going = False

    if customer != "report" and customer != "off":
        price_of_drink = float(MENU[customer]['cost'])
        # print(price_of_drink)
        print("Please insert coins:")
        quarters = float(input("How many quarters? "))
        dimes = float(input("How many dimes? "))
        nickels = float(input("How many nickels? "))
        pennies = float(input("How many pennies? "))

        price_drink()

