import requests
URL = "https://nominatim.openstreetmap.org/reverse"


def fetch_location(lat,lon):
    try:
        response = requests.get(URL, params= {"lat": lat, "lon": lon, "format":"jsonv2","zoom": 5}, headers = {"User-Agent": "iss-tracker-learning-project"}, timeout= 5)
        response.raise_for_status()
        return response.json()
    
    except requests.RequestException as e:
        print(f"Could not fetch location: {e}")
        return None

def parse_location(data):
    try:
        return data["display_name"]
    
    except (KeyError,TypeError):
        return None


def get_location(lat,lon):
    result = fetch_location(lat, lon)
    if result is None:
        return None
    return parse_location(result)



if __name__ == "__main__":
    print(parse_location(fetch_location(48.86, 2.35)))
    print(parse_location(fetch_location(0, -30)))