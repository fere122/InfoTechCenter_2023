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
        print("National Weather Service has updated your alarm by 7 Hours because of the Snowing", weatherAlert)
        print("Your VRS has been activated only letting you drive 70 MPH")
    elif weatherAlert == "Blizzard":
        print("National Weather Service has updated your alarm by 2 Hours because of the Blizzard", weatherAlert)
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
