# ---------------Object--------------------
# An Object has
#   attribute
#   behavior
#
# Example Object
#   Vehicle
#       attribute --> numOfDoors, extColor, type
#       behaviour --> drive, park, crash
#
# ---------------Class---------------------
# A Class is a blueprint of an Object
# Example of a Class
import datetime
class Vehicle:

    #class attributes --> This is an attribute that is assigned to every object


    #instance attributes --> This is an attribute that is assigned to a specific object
    # The first method in a class is a constructor __init__
    # This method is executed everytime the class is called and a new object is created
    # self -->is a reference to the object itself
    #   If we call a method in a class the object itself is the first parameter
    def __init__(self, VIN, numOfDoors, passCode, buildDate):
        self.VIN        = VIN
        self.numOfDoors = numOfDoors
        self.passCode   = passCode
        self.buildDate  = buildDate
    # instance method
    def ageOfVehicle(self):
        today = datetime.date.today()
        vehicleAge = today.year - self.buildDate.year
        return vehicleAge

    def startTheVehicle(self, keyStatus, passCode):
        if keyStatus and passCode == self.passCode:
            return 'Start the car'
        elif keyStatus:
            return 'The passcode {} for car {} is incorrect'.format(passCode, self.VIN)
        else:
            return 'The key is not present'
    
scottsBlueFord = Vehicle(
    "12345GHF",
    4,
    1234,
    datetime.date(2013, 3, 15)
)

print(scottsBlueFord.VIN)
print(scottsBlueFord.numOfDoors)
print(scottsBlueFord.ageOfVehicle())
print(scottsBlueFord.startTheVehicle(True, 1234))
print(scottsBlueFord.startTheVehicle(True, 2345))
print(scottsBlueFord.startTheVehicle(False, 1234))
