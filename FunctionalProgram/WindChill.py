import math

while True:


    temperature = int(input("Enter the Temperature from '0' to '50':"))
    if (temperature >= 0) and (temperature <= 50):
        windSpeed = int(input("Enter the Wind Speed between '3' to '120' : "))
        if (windSpeed >= 3) and (windSpeed <= 120):
            windChill = 35.74 + 0.6215 * temperature + (0.4275 * temperature - 35.75) * pow(windSpeed, 0.16);

            print("Temperature =", temperature, "\nwindSpeed =", windSpeed, "\nwind chill =", windChill)
            break

