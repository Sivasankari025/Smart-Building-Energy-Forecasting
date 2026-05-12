import requests

API_KEY = "YOUR_API_KEY"
CITY = "Chennai"

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    return {
        "city": CITY,
        "temperature": data['main']['temp'],
        "humidity": data['main']['humidity'],
        "condition": data['weather'][0]['description']
    }
