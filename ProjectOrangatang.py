
"""
Our Welcome Screen will start our program letting
drivers know that the InfoTech Center 2023 is loading
"""

#Import Libraries Here
import time
import sys
import random
from time import sleep
timeToSleep = 2

print("\nWelcome - InfoTech Center 2023\n")
time.sleep(timeToSleep)

#Add code to have the ellipsis add dot every .5 seconds
x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("InfoTech Center 2023 is loading" + "." * ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r" + message) # \r prints a carriage return first, so, message is printed on top of the previous line
    time.sleep(0.625)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\nOperating System Loaded - Retina Scanned - Access Granted")

print("\n. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n")
print(" checking current gas levels\n\n")
sleep(1)
# Import Libraries Here


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

print("\n. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n")

print("Weather Branch\n")

#Import Libraries here
import random
from time import sleep

#Create a function randomly choosing the weather from a list
def weather():
    weatherForecast = ["Snowing","Blizzard","Rain","Foggy","Windy","Icy","Sunny","Cloudy"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition
# Variable to call weather() once in our Vehicle Response System - VRS
weatherAlert = weather()

#VRS() function will allow my vehicel to respond based on the weather conditions
def vehicleResponseSystem():
    if weatherAlert == "Snowing":
        print("National Weather Service has updated your alarm by 7 Hours because of lots of snow", weatherAlert)
        print("Your VRS has been activated only letting you drive 70 MPH")
    elif weatherAlert == "Blizzard":
        print("National Weather Service has updated your alarm by 2 Hours because of the snow", weatherAlert)
        print("Your VRS has been activated DONT LEAVE YOUR HOME")
    elif weatherAlert == "Rain":
        print("National Weather Service has updated your alarm by 7 minutes weather is nice today", weatherAlert)
        print("Your VRS has been activated only drive under 75")
    elif weatherAlert == "Foggy":
        print("National Weather Service Has updated your alarm by 3 minutes", weatherAlert)
        print("Your VRS has been activated only drive under 80")
    elif weatherAlert == "Windy":
        print("National Weather Service has updated your alarm by 5 minutes weather is nice today", weatherAlert)
        print("Your VRS has been activated only drive under 90")
    elif weatherAlert == "Icy":
        print("National Weather Service has updated your alarm by 50 minutes weather is nice today", weatherAlert)
        print("Your VRS has been activated only drive under 30")
    elif weatherAlert == "Sunny":
        print("Nice day it is enjoy your drive")
    else:
        print("Nice day it is enjoy your drive to your favorite MCDONALDS")

vehicleResponseSystem()

