import math


class Controller:
    def __init__(self, initX, initY, initHeading):
        self.x = initX
        self.y = initY
        self.heading = initHeading

    def turn_cmd(self, directionX, directionY):
        # Implementation for turning command
        targetHeading = math.degrees(math.atan2(directionY, directionX))
        targetHeading = targetHeading % 360 # ensure heading is within 0-360 degrees
        turnIncrement = (targetHeading - self.heading + 180) % 360 - 180 # ensures the turn increment is between -180 and 180 degrees
        turnIncrement/=180
        turnCommand = (max(-1, min(1, turnIncrement))) # clamp the turn command between -1 and 1
        return turnCommand
        # heading is updated when timestep is applied, not when turn_cmd is called
    
    def drive_cmd(self, targetX, targetY):
        # Implementation for driving command
        distance = math.sqrt((targetX - self.x) ** 2 + (targetY - self.y) ** 2)
        if (distance <= 0.5):
            return 0 # if the target point is the same as the current position, no driving is needed
        else:
            # calculate the distance to the target point pythagorean theorem
            driveCommand = max(-1, min(1, distance)) # clamp the drive command between -1 (backwards) and 1 (forwards)
            return driveCommand
            # position is updated when timestep is applied, not when drive_cmd is called