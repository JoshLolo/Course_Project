# Course_Project
# CIS245
# Josh Lolo
# August 2022
# Script to output current weather from users input location

import json, requests

base_url ="https://api.openweathermap.org/data/2.5/weather"
appid = "e7d04e47ecfc393ac00b8810f7218e1b"
city = (input("Please enter a zipcode or city: "))

url = f"{base_url}?q={city}&units=imperial&APPID={appid}"
print(url)
print()

response = requests.get(url)
unformated_data = response.json()

try:
  print("You have succesfully connected to")
except Exception:
  print("you did not connect to the website, please try again.")
# still working on figuring this out
url =f"{base_url}?q={city}&units=imperial&APPID={appid}"
print(url)
print()

temp = unformated_data["main"]["temp"]
print(f"The current temperature in {city} is: {temp} degrees")

feels_like = unformated_data["main"]["feels_like"]
print(f"Feels like: {feels_like} degrees")

temp_max = unformated_data["main"]["temp_max"]
print(f"The max temperature is: {temp_max} degrees")
print()

wind = unformated_data["wind"]["speed"]
print(f"The current wind speed is: {wind} MPH")

pressure = unformated_data["main"]["pressure"]
print(f"The air pressure is: {pressure}")

humidity = unformated_data["main"]["humidity"]
print(f"The humidity is currently: {humidity}%")

visibility = unformated_data["visibility"]
print(f"Visibility is: {visibility}")
print()

while True:
  city = (input("Would you like to look up another city?: "))
  if city == 'yes':
    city = print(input("Please enter a zipcode or city: "))
    temp = unformated_data["main"]["temp"]
    print(f"The current temperature in {city} is: {temp} degrees")
    feels_like = unformated_data["main"]["feels_like"]
    print(f"Feels like: {feels_like} degrees")
    temp_max = unformated_data["main"]["temp_max"]
    print(f"The max temperature is: {temp_max} degrees")
    print()
    wind = unformated_data["wind"]["speed"]
    print(f"The current wind speed is: {wind} MPH")
    pressure = unformated_data["main"]["pressure"]
    print(f"The air pressure is: {pressure}")
    humidity = unformated_data["main"]["humidity"]
    print(f"The humidity is currently: {humidity}%")
    visibility = unformated_data["visibility"]
    print(f"Visibility is: {visibility}")
    print() 
    if city == 'no':
     print("Goodbye.")
    break
# This is almost done, I just need to figure out a better way to call the new input to display
