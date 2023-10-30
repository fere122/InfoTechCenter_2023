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

#Funtion will call the gaLevelGauge to determine gal level and find a close gas station if low
def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25),1)
    milesToGasStationquarterTank = round(random.uniform(25.1, 50), 1)
