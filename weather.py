import requests

API_KEY = 'a2a0ee00786928d760b2ab6dca8fe072'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

def get_weather(city):
    complete_url = BASE_URL + "q=" + city + "&appid=" + API_KEY + "&units=metric"
    response = requests.get(complete_url)
    data = response.json()

    # Print the full response for debugging purposes
    # print("Full API Response:")
    # print(data)

    if data["cod"] != "404":
        main = data.get("main", {})
        wind = data.get("wind", {})
        weather = data["weather"][0] if "weather" in data and data["weather"] else {}

        print(f"City: {city}")
        print(f"Temperature: {main.get('temp', 'N/A')}°C")
        print(f"Humidity: {main.get('humidity', 'N/A')}%")
        print(f"Weather: {weather.get('description', 'N/A')}")
        print(f"Wind Speed: {wind.get('speed', 'N/A')} m/s")
    else:
        print(f"City {city} not found. Error: {data.get('message', 'No message')}")

if __name__ == "__main__":
    city = "London"
    get_weather(city)
