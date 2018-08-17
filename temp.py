#! python3
# temp.py - convert to and from Celcius and Fahrenheit

def to_f(c):
    return ((9/5 * c) +32)

def to_c(f):
    return ((5/9) * (f - 32))

scale = "c"
scale = input("Into which scale would you like to convert? (Type F or C.) ")

if scale.lower() == 'c':
    fah = float(input("Type the temperature in Fahrenheit:  "))
    f = to_c(fah)
    print(f)
elif scale.lower() == 'f':
    cel = float(input("Type the temperature in Celcius:  "))
    c = to_f(cel)
    print(c)
else:
    print("Please type either F or C.")
