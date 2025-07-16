"""
Mostrare los numeros del 1 al 100 e intercambiare los multiplos,
de 3 por "fizz" y los de 5 por "buzz"
"""

num1 = 1

while num1 <= 100:
    print(num1)
    if num1 % 3 == 0 and num1 % 5 == 0:
        print("FizzBuzz")
    elif num1 % 3 == 0:
        print("Fizz")
    elif num1 % 5 == 0:
        print("Buzz")
    num1 = num1 + 1