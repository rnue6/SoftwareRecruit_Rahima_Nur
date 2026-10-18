import math


class Controller:
    def __init__(self, initX, initY, initHeading):
        self.x = initX
        self.y = initY
        self.heading = initHeading

    def turn_cmd(self, targetX, targetY):
        # Implementation for turning command
        targetHeading = math.degrees(math.atan2(targetY - self.y, targetX - self.x))
        targetHeading = targetHeading % 360 # ensure heading is within 0-360 degrees
        turnIncrement = (targetHeading - self.heading + 180) % 360 - 180 # ensures the turn increment is between -180 and 180 degrees
        turnIncrement/=180
        turnCommand = (max(-1, min(1, turnIncrement))) # clamp the turn command between -1 and 1
        return turnCommand
        # heading is updated when timestep is applied, not when turn_cmd is called
    
    def drive_cmd(self, distance):
        # Implementation for driving command
        if (distance <= 0.5):
            return 0 # if the target point is the same as the current position, no driving is needed
        else:
            # clamp the drive command between -1 (backwards) and 1 (forwards) to slow down the rover as it approaches the target point and prevent overshooting
            driveCommand = max(-1, min(1, distance)) 
            return driveCommand
            # position is updated when timestep is applied, not when drive_cmd is called
    
    def update_location(self, timestep, driveCommand, turnCommand):
        maxSpeed = 2.0
        driveSpeed = driveCommand * maxSpeed
        turnSpeed = turnCommand * 90 # assuming turnCommand is normalized between -1 and 1

        # update the rover's position based on its current heading and speed keeping within the bounds of 0-360 degrees
        self.heading = (self.heading + turnSpeed * timestep) % 360
        self.x += driveSpeed * math.cos(math.radians(self.heading)) * timestep
        self.y += driveSpeed * math.sin(math.radians(self.heading)) * timestep