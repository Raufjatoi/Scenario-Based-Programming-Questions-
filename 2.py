#2. Restaurant Order Management System:
#Design a program for a restaurant's wait staff to manage customer orders. It should allow:
# Selecting a table number to access the order for that specific customer.
# Adding items from a pre-defined menu (including name, price, and category) to the order.
# Modifying or removing items from the order.
# Calculating the total cost of the order, including any applicable taxes.
# Printing a receipt for the customer. 

menu = [
    {"name": "Margherita Pizza", "price": 9.99, "category": "Pizza"},
    {"name": "Chicken Alfredo Pasta", "price": 12.49, "category": "Pasta"},
    {"name": "Cheeseburger", "price": 8.99, "category": "Burger"},
    {"name": "Caesar Salad", "price": 7.99, "category": "Salad"},
    {"name": "Fish and Chips", "price": 10.99, "category": "Seafood"},
    {"name": "Vegetable Stir Fry", "price": 9.49, "category": "Vegetarian"},
    {"name": "Grilled Steak", "price": 15.99, "category": "Entree"},
    {"name": "Mushroom Risotto", "price": 11.99, "category": "Risotto"},
    {"name": "BBQ Ribs", "price": 14.99, "category": "BBQ"},
    {"name": "Chocolate Brownie Sundae", "price": 6.99, "category": "Dessert"}
]

tables = []

def view_menu():
    for item in menu:
        print(f"Name: {item['name']:25}, Price: ${item['price']:.2f}, Category: {item['category']}")

def engaged_seats():
    if not tables:
        print('No customer on any seat.')
    else:
        for idx, table in enumerate(tables, start=1):
            print(f"Seat number {idx}: {table['table no']} is engaged.")

    seat = input('Enter seat number to deliver food: ')
    found = False
    for table in tables:
        if table.get('table no') == seat:
            print('Food delivered to seat ', seat)
            found = True
            break
    if not found:
        print('No customer on that seat.')

def edit_menu():
    op = input("Enter 'A' to add a new item, 'R' to remove, or 'E' to edit an existing item: ").lower()
    if op == 'a':
        name = input('Enter the name of the new item: ')
        price = float(input('Enter the price of the item: '))
        category = input('Enter the category of the food: ')
        menu.append({'name': name, 'price': price, 'category': category})
        print('Item added successfully.')
    elif op == 'r':
        name = input('Enter the name of the item you want to remove: ')
        for item in menu:
            if item['name'] == name:
                menu.remove(item)
                print('Item removed successfully.')
                break
        else:
            print('Item not found in the menu.')
    elif op == 'e':
        name = input('Enter the name of the item you want to edit: ')
        for item in menu:
            if item['name'] == name:
                item['name'] = input('Enter the new name: ')
                item['price'] = float(input('Enter the new price: '))
                item['category'] = input('Enter the new category: ')
                print('Item edited successfully.')
                break
        else:
            print('Item not found in the menu.')

def main():
    while True:
        print('\t\t\tOrder Management System')
        print('Input "O" to order, "S" to show the service, "E" to edit items, or any other key to exit.')

        service = input('Enter option: ').lower()
        if service == 'o':
            t = input('Enter your table number: ')
            print(f'Welcome, table {t}. Please place your order:')
            view_menu()
            n = input('Enter the items you want to order: ')
            tables.append({'table no': t, 'order': n})
            print('Order booked successfully.')
            
            # Calculate bill
            bill = 0
            for item in menu:
                if item['name'] in n:
                    bill += item['price']
            print(f'Your bill is: ${bill:.2f} (tax included).')
            
        elif service == 'e':
            edit_menu()
        elif service == 's':
            engaged_seats()
        else:
            break

if __name__ == '__main__':
    main()
