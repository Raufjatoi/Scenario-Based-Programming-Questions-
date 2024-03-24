#6. Simple Fitness Tracker:
#Design a program to work with a wearable fitness tracker. It should:
# Track daily steps, distance walked, and calories burned based on user activity data.
# Allow users to set daily activity goals and monitor their progress.
# Generate reports that:
#o Compare daily activity levels over a period of time (e.g., weekly, monthly).
#o Calculate trends in user's fitness progress

daily = {'date': '1/1/2004', 'steps': 100}
weekly = [{'date': '1/1/2004', 'steps': 100}]
monthly = [{'date': '1/1/2004', 'steps': 100}]

total_cal_month = 0
total_dis_month = 0

goal_data = {}

def weeksteps():
    total = 0
    for w in weekly:
        total += w['steps']
    return total

def monthsteps():
    total = 0
    for m in monthly:
        total += m['steps']
    return total

def add_steps():
    steps_input = int(input('Enter today\'s steps: '))
    date_input = input('Enter date (e.g., 2/15/2024): ')
    daily['date'] = date_input
    daily['steps'] = steps_input
    weekly.append({'date': date_input, 'steps': steps_input})
    monthly.append({'date': date_input, 'steps': steps_input})

def distance():
    daily_distance = daily['steps'] / 2
    weekly_distance = weeksteps() / 2
    monthly_distance = monthsteps() / 2
    print(f'You traveled {daily_distance} meters today')
    print(f'Weekly wise you traveled {weekly_distance} meters')
    print(f'Monthly wise you traveled {monthly_distance} meters')

def cal():
    daily_calories = daily['steps'] / 10
    weekly_calories = weeksteps() / 10
    monthly_calories = monthsteps() / 10
    print(f'You burned {daily_calories} calories today')
    print(f'Weekly wise you burned {weekly_calories} calories')
    print(f'Monthly wise you burned {monthly_calories} calories')

def set_goal():
    print('Set your monthly fitness goals:')
    steps_goal = int(input('Enter steps goal: '))
    cal_goal = int(input('Enter calories goal: '))
    distance_goal = int(input('Enter distance goal: '))
    goal_data['steps'] = steps_goal
    goal_data['calories'] = cal_goal
    goal_data['distance'] = distance_goal

def progress():
    print(f'Your monthly steps: {monthsteps()}, Target: {goal_data["steps"]}')
    print(f'Your monthly calories burned: {total_cal_month}, Target: {goal_data["calories"]}')
    print(f'Your monthly distance: {total_dis_month}, Target: {goal_data["distance"]}')

def main():
    while True:
        print('\t\t\t SIMPLE FITNESS TRACKER')
        print('\tPlease follow below keywords to use it:')
        print('\t"A" to add data\n\t"G" to set goal\n\t"P" to see the progress\n\t"R" to see overall report\n\tAnything else to quit')
        op = input('Enter your reply: ').lower()
        if op == 'a':
            add_steps()
        elif op == 'g':
            set_goal()
        elif op == 'p':
            progress()
        elif op == 'r':
            print('\t\t The overall report is below\n')
            print('\tSTEPS')
            print(f'Daily: {daily["steps"]}')
            print(f'Weekly: {weeksteps()}')
            print(f'Monthly: {monthsteps()}\n')
            print('\tCALORIES')
            cal()
            print('\n')
            print('\tDISTANCE')
            distance()
        else:
            print('Thanks for using.')
            break

if __name__ == '__main__':
    main()
