fahrenheit = float(input("What temperature (in Fahrenheit) would you like converted to Celsius? "))

celsius = (fahrenheit - 32) * (5/9)

celsius = round(celsius,2)
print("Your temperature in Celsius is " + str(celsius) + " degrees.")
