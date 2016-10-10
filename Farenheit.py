# Olivia Bicks ohb3fs

temperature_celsuis = float(input("What is the temperature in Celsuis? "))
new_temperature_fahrenheit = format(temperature_celsuis * 9 / 5 + 32, ".1f")

print("It is", new_temperature_fahrenheit, "degrees fahrenheit")

temperature_fahrenheit = float(input("What is the temperature in Fahrenheit? "))
new_temperature_celsuis = format((5 * (temperature_fahrenheit - 32))/9, ".1f")

print("It is", new_temperature_celsuis, "degrees Celsuis")










