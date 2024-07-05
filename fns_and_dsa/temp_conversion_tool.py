FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

A = float(input("Enter the temperature to convert: "))
b = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

def convert_to_celsius(A):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{A}°F is {(A - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR}°C")
def convert_to_fahrenheit(A):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    print(f"{A}°C is {(A * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32}°F")
    
if b == "C":
    convert_to_celsius(A)
elif b == "F":
    convert_to_fahrenheit(A)
else:
    print("Invalid temperature. Please enter a numeric value.")