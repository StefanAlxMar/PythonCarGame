driver_input = ''
car_engine = False
while True:
    driver_input = input('You are in your car: ').lower()
    if driver_input == 'help':
        print("""
start - to start the car
stop - to stop the care
quit - to exit car
        """)
    elif driver_input == 'start':
        if car_engine == True:
            print('Car already started')
        else:
            print("Engine started")
            car_engine = True
    elif driver_input == 'stop':
        if car_engine == False:
            print('Engine already stopped')
        else:
            print('Engine stopped')
        car_engine = False
    elif driver_input == 'quit':
        break
    else:
        print('Incorrect command')

