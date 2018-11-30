#-------------Object-----------------
    #An Object has
        #Attribute
        #Behavior
    #Example Object
    #   car
    #       attributes -->extColor, numDoors, describing the object
    #       behavior --> start, drive, stop

#-------------Class-------------------
    # A Class is a blueprint of an Object
    # Example of class
    #  Vehicle 
    #       class attribute --> this an attribute that applies to classes
    #       instance attribute --> to the specific object that I am creating
import datetime  
class Vehicle:
    def __init__ (self, VIN, numOfDoors, buildDate):                 #-->Constructor    
        self.VIN        = VIN
        self.numOfDoors = numOfDoors
        self.buildDate  = buildDate
    def ageOfVehicle(self):
        today = datetime.date.today()
        vehicleAge = today.year - self.buildDate.year
        return vehicleAge


scottsBlueCar = Vehicle('1234', 4, datetime.date(2013, 4, 24))
scottsGreenCar = Vehicle('5678', 4, datetime.date(2014, 4, 24))
print(scottsBlueCar.VIN)
print(scottsGreenCar.VIN)
print(scottsBlueCar.buildDate)
print(scottsBlueCar.ageOfVehicle())