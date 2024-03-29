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
money = 0

def print_report(res, m):
    print(f"Water: {res['water']}ml")
    print(f"Milk: {res['milk']}ml")
    print(f"Coffee: {res['coffee']}g")
    print(f"Money: ${m}")

def resources_suff(res, order):
    if MENU[order]["ingredients"]["water"] > res["water"]:
        print("Sorry there in no enough water.")
        return False
    if order != 'espresso':
        if MENU[order]["ingredients"]["milk"] > res["milk"]:
          print("Sorry there in no enough milk.")
          return False
    if MENU[order]["ingredients"]["coffee"] > res["coffee"]:
        print("Sorry there in no enough coffee.")
        return False
    return True

def coints():
    q = int(input("how many quarters?: "))
    d = int(input("how many dimes?: "))
    n = int(input("how many nickels?: "))
    p = int(input("how many pennies?: "))
    return 0.01 * p + 0.05 * n + 0.1 * d + 0.25 *q

def chek_transaction(m, order):
    if m < MENU[order]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    return True

def make_coffee(m, order):
    global money
    money += MENU[order]["cost"]
    resources["water"] -= MENU[order]["ingredients"]["water"]
    resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
    if order != "espresso":
        resources["milk"] -= MENU[order]["ingredients"]["milk"]
    change = m - MENU[order]["cost"]
    print(f"Here is ${change:.2f} in change")
    print(f"Here is your {order}☕. Enjoy!")

is_on = True

while is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        is_on = False
    elif order == "report":
        print_report(resources, money)
    else :
        chek_res = resources_suff(resources, order)
        if chek_res:
          pay = coints()
          chek_tran = chek_transaction(pay, order)
          if chek_tran and chek_res:
              make_coffee(pay, order)
