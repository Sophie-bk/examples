"""Assignment 1 - Sophie Bieker"""

import csv
import numpy as np

OFFSET_C_TO_F = 32

FACTOR_C_TO_F = 1.8

TEMP_THRESHOLD_C = 25

PATH_WEATHER_DATA = "./../../../data/weather_data.csv"


def change_to_fahrenheit(celsius):
    """
    This function changes the temperature above 25°C from celsius to fahrenheit
    """
    temps = []
    for i in celsius:
        if float(i[1]) > TEMP_THRESHOLD_C:
            temps.append(float(i[1]) * FACTOR_C_TO_F + OFFSET_C_TO_F)
        else:
            temps.append(float(i[1]))
    return temps


# read data set
file = open(PATH_WEATHER_DATA)
ds = list(csv.reader(file))
file.close()
ds = ds[1:]  # start from second line
data = []  # create empty list
for i in ds:
    data.append([i[0], i[1], i[2], i[3], i[4]])

temp = change_to_fahrenheit(data)
total_temp = np.sum(temp)
average_temp = np.mean(temp)
print("sum of the temperatures:", total_temp)
print("average temperature:", average_temp)

def wind(ds):
    """
    This function calculates the wind speed
    """
    ws = 0
    for i in ds:
        u = float(i[3])
        v = float(i[4])
        ws += np.sqrt(u**2 + v**2)
        wind_speed = ws / len(ds)
    return wind_speed

wind_speed = wind(ds)
print("wind speed:", wind_speed)