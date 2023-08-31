# 4.1

SUN_TO_EARTH = 147000000

class Planet:
    def __init__(self, name, distance_from_sun, planet_type):
        self.name = name
        self.distance_from_sun = distance_from_sun
        self.planet_type = planet_type

    def get_distance_to_earth(self):
        return abs(self.distance_from_sun - SUN_TO_EARTH)

# 4.2

class Mercury(Planet):
    def __init__(self, name, distance_from_sun, planet_type):
        super().__init__(name, distance_from_sun, planet_type)

    @staticmethod
    def happy_new_year():
        # Assume Earth day is 24 hours
        earth_day = 24
        mercury_year = 88 * earth_day
        print(f"A year on Mercury lasts {mercury_year} hours.")

# Create an object with Mercury's real-life properties
mercury = Mercury("Mercury", 58000000, "Terrestrial")

# 4.3

class Jupiter(Planet):
    def __init__(self, name, distance_from_sun, planet_type, number_of_moons):
        super().__init__(name, distance_from_sun, planet_type)
        self.number_of_moons = number_of_moons

    @staticmethod
    def happy_new_year():
        earth_day = 24
        jupiter_year = 4383 * earth_day
        print(f"A year on Jupiter lasts {jupiter_year} hours.")

# Create an object with Jupiter's real-life properties
jupiter = Jupiter("Jupiter", 779000000, "Gas Giant", 80)

# 4.2 Mercury attributes
print(mercury.name)
print(mercury.distance_from_sun)
print(mercury.planet_type)
print(mercury.get_distance_to_earth())
mercury.happy_new_year()

# 4.3 Jupiter attributes
print(jupiter.name)
print(jupiter.distance_from_sun)
print(jupiter.planet_type)
print(jupiter.number_of_moons)
print(jupiter.get_distance_to_earth())
jupiter.happy_new_year()