import requests

#Use any weather api service
# Set the API endpoint and your API key
endpoint = "http://api.openweathermap.org/data/2.5/weather"
api_key = "YOUR_API_KEY"

# Set the location for which you want weather data
city = "Calabar"
state = "Crossriver"

# Make the API request
response = requests.get(endpoint, params={
    "q": f"{city},{state}",
    "appid": api_key
})

# Check the status code to make sure the request was successful
if response.status_code == 200:
    # Parse the response data as JSON
    data = response.json()

    # Extract the current temperature from the data
    temperature = data["main"]["temp"]

    # Convert the temperature from kelvin to fahrenheit
    temperature_f = (temperature - 273.15) * 9 / 5 + 32

    # Print the temperature
    print(f"The current temperature in {city}, {state} is {temperature_f:.2f}°F")
else:
    print("Something went wrong :(")
