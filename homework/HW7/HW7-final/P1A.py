#!/usr/bin/python3

from Markov import *

if __name__ == "__main__":
    m = Markov()
    m.load_data(file_path='./weather.csv')
    print("The probability of windy and then cloudy:")
    print(m.get_prob('windy', 'cloudy'))
