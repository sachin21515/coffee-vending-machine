
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def main():

    input_value = input('What would you like? (espresso/latte/cappuccino): ')
    if input_value == 'report':
        print(f"""
    Water: {resources['water']}ml
    Milk: {resources['milk']}ml
    coffee: {resources['coffee']}g
        """)

    else:

        def get_order(coffee_type):

            print("please insert coins")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))

            total_inserted_amount = 25 * quarters + 10 * dimes + 5 * nickels + pennies
            if total_inserted_amount > MENU[coffee_type]['cost'] * 100:
                print(f"Here is your {total_inserted_amount - MENU[coffee_type]['cost'] * 100} in change.")
                print(f"Here is your {coffee_type} Enjoy!")
                main()

            else:
                print('inserted amount is not enough, please insert correct amount')

        water = MENU[input_value]['ingredients']['water']
        coffee = MENU[input_value]['ingredients']['coffee']

        if input_value == 'espresso':
            if water <= resources['water'] and coffee <= resources['coffee']:
                resources['water'] = resources['water']-water
                resources['coffee'] = resources['coffee'] - coffee

                get_order(input_value)
            else:
                print('There is not enough ingredients')

        else:
            milk = MENU[input_value]['ingredients']['milk']
            if water <= resources['water'] and coffee <= resources['coffee'] and milk <= resources['milk']:
                resources['water'] = resources['water'] - water
                resources['coffee'] = resources['coffee'] - coffee
                resources['milk'] = resources['milk'] - milk
                get_order(input_value)
            else:
                print('There is not enough ingredients')


main()

