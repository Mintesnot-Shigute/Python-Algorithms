import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can change this t
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()

        # Extracting relevant information from the API response
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description.capitalize()}")
        print(f"Humidity: {humidity}%")
    else:
        print(f"Failed to retrieve weather information. Status code: {response.status_code}")

def main():
    print("Weather Information Retriever\n")

    # Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
    api_key = 'YOUR_API_KEY'
    city = input("Enter the city name: ")

    get_weather(api_key, city)

if __name__ == "__main__":
    main()
