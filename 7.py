# 7. Online Learning Platform:
#Imagine you are creating a program for an online learning platform. It should allow:
# Users to register and create accounts.
# Users to enroll in different courses offered on the platform (including title, description, and
#instructor information).
# Accessing course materials such as video lectures, quizzes, and assignments.
# Submitting completed assignments and receiving feedback from instructors.

courses = [{'name': 'Python Programming', 'by': 'Sir Owais', 'descrip': 'It\'s about Python programming language'}]
accounts = [{'name': 'Rauf', 'password': '1234'}]
users = [{'rauf': 'IT course', 'complete': 'not yet'}]

def register():
    name = input('Enter name: ')
    for a in accounts:
        if a['name'] == name:
            print('Perhaps this name already exists. You may choose another or login if you like.')
            return
    password = input('Enter password: ')
    accounts.append({'name': name, 'password': password})
    print(f'WELCOME {name}')

def login():
    name = input('Enter name: ')
    password = input('Enter password: ')
    for a in accounts:
        if a['name'] == name and a['password'] == password:
            print(f'Welcome back, Mr {name}')
            return
    print('Account not found.')

def enrolled():
    name = input('Enter course name: ')
    for c in courses:
        if c['name'] == name:
            print('Found it.')
            print('Added it to your profile.')
            return
    print('Course not found.')

def add_courses():
    name = input('Enter the course name: ')
    by = input('Enter by whom: ')
    des = input('Enter description: ')
    courses.append({'name': name, 'by': by, 'descrip': des})
    print('Added successfully.')

def print_courses():
    print('Courses available:')
    for c in courses:
        print(f'Name: {c["name"]}, by: {c["by"]}, description: {c["descrip"]}')

def courses_profile():
    name = input('Enter the course you want to discover: ')
    for c in courses:
        if c['name'] == name:
            print('Found the course.')
            print('\t\t COURSE INFORMATION')
            print(f'\t Course: {c["name"]} \n\t Instructor: {c["by"]} \n\t Details: {c["descrip"]} ')
            print('\t\t ENTER "a" TO ADD COURSE OR "i" TO GET ALL THE ITEMS \n \t\t OR "e" TO ENROLL OR ANYTHING ELSE TO IGNORE')
            op = input('Enter your option: ').lower()
            if op == 'a':
                add_courses()
            elif op == 'i':
                print('Here are all the slides, assignments, and everything.')
            elif op == 'e':
                enrolled()
            else:
                print('So you typed anything else.')
            return
    print('Course not found.')

def submit():
    name = input('Enter the course name: ')
    by = input('Enter the name of instructor: ')
    for c in courses:
        if c['name'] == name:
            print('Submitted successfully.')
            return
    print(f'Didn\'t find any course named {name}.')

def main():
    while True:
        print('\t\t\t ONLINE LEARNING PLATFORM ')
        print_courses()
        start = input('Enter "r" to register if you don\'t have an account  \n or "l" to login if you have an account: ').lower()
        if start == 'r':
            register()
        elif start == 'l':
            login()
        else:
            print('Please enter a valid option.')
            break
        
        print("\t\t\t YOUR DASHBOARD")
        print_courses()
        print('\t\t ENTER "s" TO SUBMIT THE COURSES  \n \t\t ENTER "a" TO ADD COURSES \n \t\t ENTER "c" TO DISCOVER \n \t\t Or anything else to quit.')
        op = input('\t CHOOSE OPTIONS: ' ).lower()
        if op == 's':
            submit()
        elif op == 'a':
            add_courses()
        elif op == 'c':
            courses_profile()
        else:
            print('Thanks for using the app.')
            break

if __name__ == '__main__':
    main()
