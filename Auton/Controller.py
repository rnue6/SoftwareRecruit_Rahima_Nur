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