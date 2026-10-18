
from Auton import Controller


# prompt user for input
startingX = float(input("Enter the rover's starting X coordinate: "))
startingY = float(input("Enter the rover's starting Y coordinate: "))
startingHeading = float(input("Enter the rover's starting heading (in degrees): "))
waypointsNum = float(input("Enter the number of waypoints to traverse: "))
controller = Controller(startingX, startingY, startingHeading)
timestep = 0.1
waypointsInOrder = []

for i in range(int(waypointsNum)):
    waypointX = float(input(f"Enter the X coordinate for waypoint {i + 1}: "))
    waypointY = float(input(f"Enter the Y coordinate for waypoint {i + 1}: "))
    waypointsInOrder.append([waypointX, waypointY])

for waypoint in waypointsInOrder:
    controller.turn_cmd(waypoint[0], waypoint[1])
    controller.drive_cmd(waypoint[0], waypoint[1])