#4. Smart Home Automation System:
#Imagine you are creating a program for a smart home device. It should be able to:
# Control various smart home features based on user input or pre-programmed schedules, such
#as:
#o Adjusting lighting (on/off, brightness, color)
#o Setting room temperature
#o Locking/unlocking doors
# Respond to user voice commands for controlling these features.

lights = {'kitchen': {'status': 'off', 'brightness': 50, 'color': 'white'},
          'living_room': {'status': 'off', 'brightness': 50, 'color': 'white'}}
temperature = 70  # Default room temperature in Fahrenheit
doors = {'front_door': 'locked', 'back_door': 'locked'}

def adjust_lighting(room, status, brightness=50, color='white'):
    if room in lights:
        lights[room]['status'] = status
        lights[room]['brightness'] = brightness
        lights[room]['color'] = color
        print(f"Lighting in {room} adjusted: Status - {status}, Brightness - {brightness}, Color - {color}")
    else:
        print(f"No light found in {room}")

def set_temperature(temp):
    global temperature
    temperature = temp
    print(f"Room temperature set to {temp}°F")

def lock_door(door):
    if door in doors:
        doors[door] = 'locked'
        print(f"{door.capitalize()} locked")
    else:
        print(f"No such door named {door}")

def unlock_door(door):
    if door in doors:
        doors[door] = 'unlocked'
        print(f"{door.capitalize()} unlocked")
    else:
        print(f"No such door named {door}")

def voice_command(command):
    if 'lights' in command:
        if 'on' in command:
            adjust_lighting('kitchen', 'on')
            adjust_lighting('living_room', 'on')
        elif 'off' in command:
            adjust_lighting('kitchen', 'off')
            adjust_lighting('living_room', 'off')
    elif 'temperature' in command:
        temp = int(command.split()[-1])
        set_temperature(temp)
    elif 'lock' in command:
        door = command.split()[-1]
        lock_door(door)
    elif 'unlock' in command:
        door = command.split()[-1]
        unlock_door(door)
    else:
        print("Command not recognized")

# testin
adjust_lighting('kitchen', 'on', brightness=70, color='warm white')
set_temperature(72)
lock_door('front_door')
unlock_door('back_door')
voice_command("Turn on lights")
voice_command("Set temperature to 68 degrees")
voice_command("Lock front door")
