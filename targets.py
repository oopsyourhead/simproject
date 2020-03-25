class Target:
    def __init__(self, location, speed, power):
        self.location = location
        self.speed = speed
        self.power = power

    def change_location(self, new_location, target_list):
        self.location = new_location
        target_locations = [o.location for o in target_list]
        return target_locations

    def change_power(self, new_power, target_list):
        self.power = new_power
        target_power = [o.power for o in target_list]
        return target_power

    def change_speed(self, new_speed, target_list):
        self.speed = new_speed
        target_speeds = [o.speed for o in target_list]
        return target_speeds