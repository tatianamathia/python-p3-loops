#!/usr/bin/env python3

def happy_new_year():
    number = 10  
    while number >= 1:  
        print(number)  
        number -= 1  
    print("Happy New Year!")  

def square_integers(integers_list):
    squared_list = []  
    for number in integers_list: 
        squared_list.append(number ** 2)  
    return squared_list  

def fizzbuzz():
    for i in range(1, 101): 
        if i % 3 == 0 and i % 5 == 0:  
            print("FizzBuzz")
        elif i % 3 == 0:  
            print("Fizz")
        elif i % 5 == 0: 
            print("Buzz")
        else:
            print(i)  
