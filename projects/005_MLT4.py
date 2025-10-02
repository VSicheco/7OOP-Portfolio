menu = {
    "taco": 5.33,
    "hotdog": 4.00,
    "fishball": 2.69,
    "siomai": 3.28,
    "nachos": 4.50,
    "sisig": 6.50,
    "fries": 2.50,
    "sandwich": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25
}

orders = []
orders_price = []

def display_menu():
    print("---------------Menu---------------")
    print("taco\t\t: ₱%.2f" % menu["taco"])
    print("hotdog\t\t: ₱%.2f" % menu["hotdog"])
    print("fishball\t: ₱%.2f" % menu["fishball"])
    print("siomai\t\t: ₱%.2f" % menu["siomai"])
    print("nachos\t\t: ₱%.2f" % menu["nachos"])
    print("sisig\t\t: ₱%.2f" % menu["sisig"])
    print("fries\t\t: ₱%.2f" % menu["fries"])
    print("sandwich\t: ₱%.2f" % menu["sandwich"])
    print("pretzel\t\t: ₱%.2f" % menu["pretzel"])
    print("soda\t\t: ₱%.2f" % menu["soda"])
    print("lemonade\t: ₱%.2f" % menu["lemonade"])
    print("----------------------------------")
def add_orders():
    while True:
        choice = input("Select an item (q to quit): ").lower()
        if choice == 'q':
            break

        if choice in menu:
            orders.append(choice)
            orders_price.append(menu[choice])
        else:
            print("Not Available")

def calculate_total():
    total = 0.00
    for amount in orders_price:
        total = total + amount
    print(f"Total is: {total:.2f}")

def display_orders():
    print("---------------Orders---------------")
    print(orders)

def main():
    display_menu()
    add_orders()
    display_orders()
    calculate_total()

main()