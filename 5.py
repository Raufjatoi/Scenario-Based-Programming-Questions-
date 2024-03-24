#5. E-commerce Product Search and Filtering:
#Develop a program for an e-commerce website's product search functionality. It should allow users to:
# Search for products using keywords or browsing by category (e.g., electronics, clothing, books).
# Filter search results based on various criteria, such as:
#o Price range
#o Brand
#o Product features
#o Customer rating

products = {
    'rolex': {'price': '$1200', 'brand': 'Rolex 10.3', 'features': 'Good at showing time', 'rating': '7.7', 'category': 'electronics'},
    'lenovo': {'price': '$1000', 'brand': 'Lenovo ideapad', 'features': 'Good for programming', 'rating': '8.0', 'category': 'electronics'},
    'iphone': {'price': '$999', 'brand': 'Apple', 'features': 'iOS operating system', 'rating': '8.5', 'category': 'electronics'},
    'samsung_tv': {'price': '$1500', 'brand': 'Samsung', 'features': '4K UHD resolution', 'rating': '9.0', 'category': 'electronics'},
    'sony_headphones': {'price': '$300', 'brand': 'Sony', 'features': 'Noise-cancellation technology', 'rating': '8.2', 'category': 'electronics'},
    'nike_shoes': {'price': '$120', 'brand': 'Nike', 'features': 'Air cushioning', 'rating': '9.1', 'category': 'clothing'},
    'kindle': {'price': '$90', 'brand': 'Amazon', 'features': 'E-ink display', 'rating': '8.8', 'category': 'electronics'},
    'logitech_mouse': {'price': '$50', 'brand': 'Logitech', 'features': 'Wireless connectivity', 'rating': '8.0', 'category': 'electronics'},
    'fitbit_watch': {'price': '$150', 'brand': 'Fitbit', 'features': 'Fitness tracking', 'rating': '8.6', 'category': 'electronics'},
    'canon_camera': {'price': '$600', 'brand': 'Canon', 'features': '24MP sensor', 'rating': '9.2', 'category': 'electronics'}
}

def search():
    s = input('Search: ').lower()
    found = False
    for key, value in products.items():
        if s in key.lower():
            print(f"{key} - Brand: {value['brand']}, Price: {value['price']}, \n Features: {value['features']}, Rating: {value['rating']}, \n Category: {value['category']}")
            found = True
    if not found:
        print(f"No item with '{s}' found.")

def search_by_cat():
    print("Enter 'e' for electronic items, 'c' for clothing items, and 'b' for books items.")
    choice = input('Enter choice: ').lower()
    found = False
    for key, value in products.items():
        if value['category'].startswith(choice):
            print(f"{key} - Brand: {value['brand']}, Price: {value['price']}, \n Features: {value['features']}, Rating: {value['rating']}")
            found = True
    if not found:
        print(f"No items found in the category '{choice}'.")

def main ():
    while True:
        print('\t\t\t E- commerence product search and filtering 🛒')
        print('\t products avaliable : ')
        for key, value in products.items():
            print(f'\t > {key}')
        op = input('Enter "s" to search items or cs to search by category :  ').lower()
        if op == 's':
            search()
        elif op == 'cs':
            search_by_cat()
        else:
            print('thanks for comin cya ')
            break

if __name__ == '__main__':
    main()



       
