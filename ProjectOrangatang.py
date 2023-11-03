print("\n. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n")

print("Weather Branch\n")

#Import Libraries here
import random
from time import sleep

#Create a function randomly choosing the weather from a list
def Weather():
    WeatherForecast = ["Snowing","Blizzard","Rain","Foggy","Windy","Icy","Sunny","Cloudy"]
    WeatherCondition = random.choice(WeatherForecast)
    return WeatherCondition
        

