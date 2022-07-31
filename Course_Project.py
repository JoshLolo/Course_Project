# Course_Project
# CIS245
# Josh Lolo
# July 2022
# Script to output current weather from users input location

import json, requests

base_url ="https://api.openweathermap.org/data/2.5/weather"
appid = "e7d04e47ecfc393ac00b8810f7218e1b"
city = input("Please enter a city or zipcode: ")

url =f"{base_url}?q={city}&units=imperial&APPID={appid}"
print(url)

response = requests.get(url)
unformated_data = response.json()

temp = unformated_data["main"]["temp"]
print(f"The current temperature is: {temp}")

temp_max = unformated_data["main"]["temp_max"]
print(f"The max temperature is: {temp_max}")


