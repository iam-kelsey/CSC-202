# CPE 202 Lab 2
# Kelsey Nguyen
# Section 07

#represents a location using name, latitude, and longitutde
#Location str, latitude int, longtitude int --> str, int, int
class Location:
    # location is a string, representing a location name
    # latitude is an int, representing latitude in degrees (-90 to 90)
    # longitude is an int representing longitude in degrees (-180 to 180)
    def __init__(self, name, lat, lon):
        self.name = name    # name of a Location
        self.lat = lat      # latitude in degrees (-90 to 90)
        self.lon = lon      # longitude in degrees (-180 to 180)

    def __eq__(self, other):
        return ((self.name == other.name) and (self.lat == other.lat) and (self.lon == other.lon))

    def __repr__(self):
        return ("Location({0!r}, {1!r}, {2!r})".format(self.name, self.lat, self.lon))

#prints information associated with Location objects
def main():
    loc1 = Location("SLO", 35.3, -120.7)
    loc2 = Location("Paris", 48.9, 2.4)
    loc3 = Location("SLO", 35.3, -120.7)
    loc4 = loc1
    print("Location 1:",loc1.lat)
    print("Location 2:",loc2)
    print("Location 3:",loc3)
    print("Location 4:",loc4.lat)

    print("\nLocation 1 equals Location 2:",loc1==loc2)
    print("Location 1 equals Location 3:",loc1==loc3)
    print("Location 1 equals Location 4:",loc1==loc4)

    locations = [loc1, loc2]
    print(loc1 in locations)
    print(loc2 in locations)
    print(loc3 in locations)
    print(loc4 in locations)
    
    loc4.lat = 41.67
    print("Loocation 4 after updated latitude:",loc4)
    print("Loocation 1 after updated latitude of Location 4:",loc4)

if __name__ == "__main__":
    main()