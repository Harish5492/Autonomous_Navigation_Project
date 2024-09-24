import time

def move_robot(direction):
    if direction == 'forward':
        print("Moving forward")
    elif direction == 'left':
        print("Turning left")
    elif direction == 'right':
        print("Turning right")
    elif direction == 'stop':
        print("Stopping")

def detect_obstacle(sensor_data):
    return sensor_data < 20  # Example threshold

def navigate():
    while True:
        distance = 15  # Simulated sensor data
        if detect_obstacle(distance):
            move_robot('stop')
            move_robot('left')
            time.sleep(1)
        else:
            move_robot('forward')
        time.sleep(0.1)
