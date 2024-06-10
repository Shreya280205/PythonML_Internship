def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

if __name__ == "__main__":
    # Input the temperature and unit from the user
    temperature = float(input("Enter the temperature: "))
    unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").upper()

    if unit == 'C':
        # Convert Celsius to Fahrenheit
        converted_temperature = celsius_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {converted_temperature}°F")
    elif unit == 'F':
        # Convert Fahrenheit to Celsius
        converted_temperature = fahrenheit_to_celsius(temperature)
        print(f"{temperature}°F is equal to {converted_temperature}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
