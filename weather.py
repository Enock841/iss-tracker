import requests
URL = "https://api.open-meteo.com/v1/forecast"


def fetch_weather(lat,lon):
    try:
        response = requests.get(URL,params={"latitude":lat,"longitude":lon,"current":"temperature_2m,cloud_cover,wind_speed_10m"},timeout=5)
        response.raise_for_status()
        data = response.json()
        return data
    
    except requests.RequestException as e:
        print(f"Could not fetch weather: {e}")
        return None


def parse_weather(data):
    try:
        current = data["current"]
        temp = current["temperature_2m"]
        cloud = current["cloud_cover"]
        wind = current["wind_speed_10m"]

        return temp,cloud,wind

    except (KeyError,ValueError, TypeError) as e:
        print(f"Could not parse weather: {e}")
        return None


def format_weather(temp,cloud,wind):
    return f"{temp}°C, {cloud}% cloud,{wind} km/h wind"


if __name__ == "__main__":
    weather = fetch_weather(51.5, -0.12)
    if weather is None:
        print("No weather data")
    else:
        result = parse_weather(weather)
        if result is None:
            print("Skipping bad weather")
        else:
            temp, cloud, wind = result
            print(format_weather(temp, cloud, wind))