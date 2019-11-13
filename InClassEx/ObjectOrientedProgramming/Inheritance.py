

import datetime  
class Vehicle:

    TYPES_OF_VEHICLES = [   'Road Vehicle' ,
                            'Air Vehicle'  ,
                            'Water Vehicle',
                            'Space Vehicle']

    def __init__ (self, typeOfVehicle, buildDate, extColor):                 #-->Constructor    
        if typeOfVehicle not in self.TYPES_OF_VEHICLES:
            raise ValueError("%s is not a valid vehicle." % typeOfVehicle)
        self.buildDate  = buildDate
        self.extColor = extColor
    def ageOfVehicle(self):
        today = datetime.date.today()
        vehicleAge = today.year - self.buildDate.year
        return vehicleAge
    def repaintVehicle(self, newColor):
        self.extColor = newColor

#------------Inheritance------------
    #Creating a new class that uses the attributes of another class
    # Parent Class  --> Child Class
    # Existing Class--> Derived Class
class RoadVehicle(Vehicle):

    typeOfVehicle = 'Road Vehicle'

    def __init__(self, buildDate, extColor, numberOfDoors, numberOfWheels):
        
        self.numberOfDoors = numberOfDoors
        self.numberOfWheels = numberOfWheels
        super(RoadVehicle, self).__init__(self.typeOfVehicle, buildDate, extColor)

scottsFancyCar = RoadVehicle(datetime.date(2014, 4, 24),'red',2,4)
print("Scott's Fancy Car")
print ('Number of Doors: ',scottsFancyCar.numberOfDoors)
print ('Type of Vehicle: ',scottsFancyCar.typeOfVehicle)
print ('Age of Vehicle:', scottsFancyCar.ageOfVehicle())
print ('Color of Vehicle:' + scottsFancyCar.extColor)
scottsFancyCar.repaintVehicle('green')
print ('Color of Vehicle:' + scottsFancyCar.extColor)
    