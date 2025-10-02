cart = []

def add_to_cart():
  item = ''
  while (item != 'x'):
    item = input("Enter x to exit or add an item to your cart: ")
    if item != 'x':
      cart.append(item)
      print(f"{item} has been added to your cart.")

def search_cart():
  item_to_find = input("Enter item you want to search: ")
  item_found = 0
  if item_to_find in cart:
    item_found = item_found + 1
  else:
    print(f"{item_to_find} is not in your cart.")
  print(f"{item_to_find} found {item_found} time(s) in your cart.")

def remove_from_cart():
  item_to_remove = input("Enter item you want to remove: ")
  if item_to_remove in cart:
    cart.remove(item_to_remove)
    print(f"Item found and deleted: {item_to_remove}")
  else:
    print(f"Item not found-deletion unsuccessful: {item_to_remove}")

def view_cart():
  print("Items in your cart:")
  for item in cart:
    print(item)

def menu():
  choice = ''
  while (choice != 0):
    print("\nMenu:")
    print("1. Add to cart")
    print("2. Search cart")
    print("3. Remove from cart")
    print("4. View cart")
    print("5. Sort cart")
    print("0. Exit")
    choice = int(input("Enter your choice (0-5): "))
    
    if choice == 1:
      add_to_cart()
    elif choice == 2:
      search_cart()
    elif choice == 3:
      remove_from_cart()
    elif choice == 4:
      view_cart()
    elif choice == 5:
      cart.sort()
      print("Cart sorted.")
    elif choice == 0:
      print("Exiting the program.")
    else:
      print("Invalid choice. Please try again.")

menu()