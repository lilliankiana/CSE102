# Author: Lillian Elliott
# Date: 11/28/2022
# q2.py
# This program gets a number a produces a response in accordance with that number

number = int(input("Enter a number: "))

if number%5 == 0:
    if number%3 == 0:
        print("FizzBuzz")
    else:
        print("Buzz")
elif number%3 == 0:
    print("Fizz")
else:
    print("The number ", number, " is NOT divisible by 3 or 5 : (")
