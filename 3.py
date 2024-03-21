#3. Personal Budget Tracker:
#Develop a program to help users manage their personal budget. It should allow:
# Setting up categories for different types of expenses (e.g., rent, groceries, transportation).
# Adding income and expenses with details like category, date, and amount.
# Generating reports that:
#o Track income and expenses over a chosen period (e.g., monthly, weekly).
#o Analyze spending by category to identify areas where the user can save.
#o Compare income and expenses to calculate the user's overall financial health.
import date
expenses = [{'rent': 100, 'groceries': 50, 'transportation': 230}]
income = [{'date':20/2/2024, 'income': 1000}]

## using defs to make it less complicative 
def total_expense():
    total = 0
    for i in expenses:
        total+=i['rent']
        total+=i['groceries']
        total+=i['transportation']
    return total    

def total_expense_week():
    total = 0
    iteration = 0
    for i in expenses:
        total += i['rent']
        total += i['groceries']
        total += i['transportation']
        iteration +=1 
        if iteration == 7:
            break
    return total

def spend_on_rent():
    total = 0
    for i in expenses:
        total += i['rent']
    return total
def spend_on_groceries():
    total = 0
    for i in expenses:
        total += i['groceries']
    return total
def spend_on_transportation():
    total = 0
    for i in expenses:
        total += i['transportation']
    return total

def spend_on_rent_week():
    total = 0
    c = 0
    for i in expenses:
        total += i['rent']
        c += 1
        if c == 7:
            break
    return total
def spend_on_groceries_week():
    total = 0
    c = 0
    for i in expenses:
        total += i['groceries']
        c += 1
        if c == 7:
            break
    return total
def spend_on_transportation_week():
    total = 0
    c = 0
    for i in expenses:
        total += i['transportation']
        c += 1
        if c == 7:
            break
    return total

def add():
    rent = int(input('Enter rent expense : '))
    groceries = int(input('Enter groceries expense : '))
    transportation = int(input('Enter transprtation expense : '))
    


