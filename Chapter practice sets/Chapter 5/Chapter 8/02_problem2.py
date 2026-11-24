# 2. Write a python program using function to convert Celsius to Fahrenheit.
def temp_conv(cel):
    ferhanite =(cel * 1.8)+32
    return ferhanite 

celcius = float(input("Enter your temp in celcius: "))
f = temp_conv(celcius)
print(f"The conversion of your {celcius}degree celcius to ferhanite is {f}")
