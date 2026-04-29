import math as mt # to import the library math and making a shortform to be able to use it efficiently
num = int(input("Enter a number: ")) #taking input
if num>0:
    print("Square root: ", mt.sqrt(num))
    print("Logarithm: ", mt.log(num))
    print("Sine: ", mt.sin(num))
else:
    print("Invalid input!!")