print("***********************************************")
print("Gasoline Branch\n\n")

# Import Libraries Here
import random
from time import sleep

# Function that list random gas stations, and Return its value
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Function with a list of GasStations
def listOfGasStations():
    gasStations = ["Shell","Speedway","Exxon","Meijer","Costco","Marathon","BP","Circle K","Wesco"]
    gasStationNearby = random.choice(gasStations)
    return gasStationNearby

#Funtion will call the gaLevelGauge to determine gal level and find a close gas station if low
def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25),1)
    milesToGasStationquarterTank = round(random.uniform(25.1, 50), 1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***")
        sleep(1.2)
        print("Calling Triple AAA")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking google maps for closest gas station.")
        sleep(1.55)
        print("The closest gas station is.",listOfGasStations(),"whitch is",milesToGasStationLow,"Miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("You have a quarter of a tank of gasoline, checking google maps for the closest gas stations.")
        sleep(1.5)
        print("The closest gas station is",listOfGasStations(),"which is",milesToGasStationquarterTank,"miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank has half of a tank which is plenty to get to MC Donalds.")
    elif gasLevelIndicator == "Three Quater Tank":
        print("Your gas tank is at three quarter tank!!!")
    else:
        print("Your gas tank is full - YOU SHOULD LEAVE THE HOUSE MORE")


gasLevelAlert()



