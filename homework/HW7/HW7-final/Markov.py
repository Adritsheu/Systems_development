#!/usr/bin/python3

import numpy as np
import pandas as pd

class Markov():
    def __init__(self, day_zero_weather = None): # You will need to modify this header line later in Part C
        self.data = np.array([[]])
        self.weather_map = {'sunny': 0, 'cloudy': 1, 'rainy':2, 'snowy':3, 'windy':4, 'hailing': 5}
        self.day_zero_weather = day_zero_weather
        self._current_day = 0
        
        # used to store values for iteration
        self._current_day_weather = day_zero_weather
        self._next_day_weather = day_zero_weather
        

    def load_data(self, file_path='./weather.csv'):
        self.data = np.genfromtxt(file_path, delimiter = ",")

    def get_prob(self, current_day_weather, next_day_weather):
    # forces lowerc ase
        current_day = current_day_weather.lower()
        next_day = next_day_weather.lower()
              
        if current_day in self.weather_map.keys():
            i = self.weather_map.get(current_day)
            if next_day in self.weather_map.keys():
                j = self.weather_map.get(next_day)
            else:
                raise Exception("Next Day Weather not in list of weather")
        else:
            raise Exception("Current Day Weather not in list of weather")
            
        return self.data[i][j]
    
    def __iter__(self):
        return MarkovIterator(self, self.today)
    
    
    def _simulate_weather_for_day(self,day):
        '''Need to get weather for day specified to add'''
        if day == 0:
            return self._current_day_weather
        elif day > 0:
            self._current_day = 0
            self._current_day_weather = self.day_zero_weather
            
            while self._current_day <= day:
                self._next_day_weather = next(iter(MarkovIterator(self, self._current_day_weather)))
                
                self._current_day_weather = self._next_day_weather
                self._current_day += 1

            #should give us the weather of the correct day
            return self._next_day_weather
        else:
            raise ValueError("Day must be non negative")

    def get_weather_for_day(self, day, trials = 100):
        '''List of weather for the specified day and done a certain amount of trials'''
        i = 0
        weather_list = []
        
        while i < trials:
            weather_list.append(self._simulate_weather_for_day(day))
            i += 1
        return weather_list

    

class MarkovIterator:
    #put the super inherit
    def __init__(self, m: Markov, day_zero_weather):
        self.m = m
        self.today = day_zero_weather

    def __iter__(self):
        return self

    def __next__(self):
        if self.today in self.m.weather_map.keys():
            index = self.m.weather_map.get(self.today)
            row = self.m.data[index, :]
            tomorrow_state = np.random.choice(6,1,p = row)
            val = tomorrow_state[0]

            for weather, index in self.m.weather_map.items():
                if val == index:
                    self.today = weather
                    return self.today
        else:
            raise Exception("Current Day is not in list of weather")

       

