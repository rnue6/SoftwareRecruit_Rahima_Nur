
import math
import time

import Controller

# While this is a simple implementation of a rover guidance system, it does not account for obstacles or other environmental factors that may affect the rover's movement
# for example, the Utah desert is not an ideally smooth/flat terrain, meaning new functions would have to be implemented in order to ensure the rover can progress without getting stuck. Furthermore,
# this rover guidance system assumes no obstacles are blocking the rover's path or changing the terrain. In a real world scenario, the rover would have to be able to navigate around things like
# rock formations, sand dunes, and deal with changes in terrain caused by weather conditions/altitude changes. One method of accounting for this could be to implement sensors and cameras that can monitor
# these kinds of obstacles and execute new commands to ensure safe navigation to the waypoints.

# prompt user for input
startingX = float(input("Enter the rover's starting X coordinate: "))
startingY = float(input("Enter the rover's starting Y coordinate: "))
startingHeading = float(input("Enter the rover's starting heading (in degrees): "))
waypointsInOrder = []

while True:
    waypointsNum = int(input("Enter the number of waypoints to traverse, 0 to exit: "))
    if waypointsNum == 0:
        break
    # initialize the controller with the starting position and heading
    controller = Controller.Controller(startingX, startingY, startingHeading)
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
            print(f"Current position: X = {controller.x:.2f}, Y = {controller.y:.2f}, Heading = {controller.heading:.2f}, Distance to waypoint {waypointsInOrder.index(waypoint) + 1} = {distance:.2f}")
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
