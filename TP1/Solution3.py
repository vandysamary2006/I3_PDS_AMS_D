def celsius_to_fahrenheit(celsius , round_to=1):    
    fahrenheit =  celsius* 9/5 + 32
    return fahrenheit  
print(celsius_to_fahrenheit(5),"F")
print(celsius_to_fahrenheit(100),"F")

def farenheit_to_celsius(fahrenheit , round_to=1):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print(farenheit_to_celsius(100),"C")
print(farenheit_to_celsius(41),"C")
print(farenheit_to_celsius(37),"C")

print("\n  °C  |   °F")
print("------+-------") 
for c in range(0,100,20): 
    print(f"{c:5} | {celsius_to_fahrenheit(c):5}")