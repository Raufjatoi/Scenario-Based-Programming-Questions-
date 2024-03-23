#3. Personal Budget Tracker:
#Develop a program to help users manage their personal budget. It should allow:
# Setting up categories for different types of expenses (e.g., rent, groceries, transportation).
# Adding income and expenses with details like category, date, and amount.
# Generating reports that:
#o Track income and expenses over a chosen period (e.g., monthly, weekly).
#o Analyze spending by category to identify areas where the user can save.
#o Compare income and expenses to calculate the user's overall financial health.
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

def total_income():
    total = 0
    for i in income:
        total += i['income']
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
    expenses.append({'rent': rent, 'groceries': groceries, 'transportation': transportation})

def incomeadd():
    date = int(input('Enter Date : '))
    incomey = int(input('Enter income : '))
    income.append({'date': date, 'income': incomey})

def stato():
    if total_income() > total_expense():
        print(f'Your total expense {total_expense()} is less then your income {total_income()} ')
        print(f'Thats good u saved {total_income()- total_expense()} rupees')
    elif total_income() < total_expense():
        print(f'Your total expense {total_expense()} is greater then your income {total_income()}')
        print(f'Thas not so good want to knoe more bout it "y" or "not" ')
        op = input('Enter ur reply : ').lower()
        if op == 'y':
            print('.....')
        elif op == 'n':
            print('bye :|')
        else:
            pass
def main():
    while True:
        print('\t\t\t Personal BUdget tracker ')
        op = input('Enter A to  add expense or B to add income or R to see the report or anythin else to quite ').lower()
        if op == 'a':
            add()
        elif op == 'b':
            incomeadd()
        elif op == 'r':
            a = input('enter the "w" if you want to see in weekely total or "A" to see all the total \n or you can input "f" to see the financial condition : ').lower()
            if a == 'a':
                print(f'grocies total : {spend_on_groceries()}')
                print(f'transportation totl : {spend_on_transportation()}')
                print(f'rent total : {spend_on_rent()}')
            elif a == 'w':
                print(f'weekely total on grocieries {spend_on_groceries_week()}:')
                print(f'weekely total on grocieries {spend_on_transportation_week()}:')
                print(f'weekely total on grocieries {spend_on_rent_week()}:')
            elif a == 'f':
                stato()
            else:
                pass
        else:
            print('Thanks for using our app ')
            break
if __name__ == '__main__':
    main()
