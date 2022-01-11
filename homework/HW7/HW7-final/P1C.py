#!/usr/bin/python3

from Markov import *
from collections import Counter
import json


# from stack overflow
def most_common(lst):
    return max(set(lst), key=lst.count)

city_weather = {
    'New York': 'rainy',
    'Chicago': 'snowy',
    'Seattle': 'rainy',
    'Boston': 'hailing',
    'Miami': 'windy',
    'Los Angeles': 'cloudy',
    'San Francisco': 'windy'
}


print("Most likely weather in seven days from the current day")
print("--------------------------------")
for key, value in city_weather.items():
    m = Markov(city_weather.get(key))
    m.load_data(file_path='./weather.csv')
    city_list = m.get_weather_for_day(7, 100 )
    print(f"{key}: {most_common(city_list)}")
    
    
print(" \n")


print("Number of occurrences of each weather condition over the 100 trials for each city 7 days from the current day")
print("--------------------------------")
for key, value in city_weather.items():
    m = Markov(city_weather.get(key))
    m.load_data(file_path='./weather.csv')
    city_list = m.get_weather_for_day( 7, 100 )
    count_list = Counter(city_list)
    sorted_list = json.dumps(count_list)
    print(f"{key} : {sorted_list}")
