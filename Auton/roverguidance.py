
import math
import time

from Auton import Controller


# prompt user for input
startingX = float(input("Enter the rover's starting X coordinate: "))
startingY = float(input("Enter the rover's starting Y coordinate: "))
startingHeading = float(input("Enter the rover's starting heading (in degrees): "))
waypointsInOrder = []

while True:
    waypointsNum = int(input("Enter the number of waypoints to traverse: "))
    # initialize the controller with the starting position and heading
    controller = Controller(startingX, startingY, startingHeading)
    timestep = 0.1

    # prompt user for waypoint coordinates
    for i in range(int(waypointsNum)):
        waypointX = float(input(f"Enter the X coordinate for waypoint {i + 1}: "))
        waypointY = float(input(f"Enter the Y coordinate for waypoint {i + 1}: "))
        waypointsInOrder.append([waypointX, waypointY])

    # for each waypoint, calculate the distance and turn/drive commands until the rover reaches the waypoint
    for waypoint in waypointsInOrder:
        distance = ((waypoint[0] - controller.x) ** 2 + (waypoint[1] - controller.y) ** 2) ** 0.5
        
        while distance > 0.5:
            headingError = (math.degrees(math.atan2(waypoint[1] - controller.y, waypoint[0] - controller.x)) - controller.heading + 180) % 360 - 180
            
            # if heading error is greater than 45 degrees, stop driving to prevent circling the waypoint
            if abs(headingError) > 45:
                driveCommand = 0
            else:
                driveCommand = controller.drive_cmd(distance)
            turnCommand = controller.turn_cmd(waypoint[0], waypoint[1])
            controller.update_location(timestep, driveCommand, turnCommand)
            time.sleep(timestep)
            distance = ((waypoint[0] - controller.x) ** 2 + (waypoint[1] - controller.y) ** 2) ** 0.5

    # after all waypoints have been traversed, print the final position and heading of the rover. 
    # set the last x and y position and heading as the new starting position and heading for the next iteration
    # reset movement commands
    driveCommand = 0
    turnCommand = 0
    controller.update_location(timestep, driveCommand, turnCommand)
    print("Waypoint traversal complete. Final position: X =", controller.x, ", Y =", controller.y, ", Heading =", controller.heading)
    startingX = controller.x
    startingY = controller.y
    startingHeading = controller.heading
    waypointsInOrder.clear()
