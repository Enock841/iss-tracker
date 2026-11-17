from datetime import datetime, timezone
import requests
URL = "http://api.open-notify.org/iss-now.json"

def fetch_iss_data():
    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data
    
    except requests.RequestException as e:
        print(f"Could not fetch data: {e}")
        return None


def parse_position(response):

    try:

        lat = float(response["iss_position"]["latitude"])
        lon = float(response["iss_position"]["longitude"])

        ts = response["timestamp"]
        when = datetime.fromtimestamp(ts, tz=timezone.utc)

        return lat,lon,when
    
    except (KeyError,ValueError,TypeError) as e:
        print(f"Could not parse response: {e}")
        return None


data = fetch_iss_data()
if data is None:
    print("No data, try again later")
else:
    result = parse_position(data)
    if result is None:
        print("Skipping bad response")
    else:
        lat,lon,when = result
        print(f"The ISS is at {lat:.2f}, {lon:.2f} as of {when.strftime('%H:%M:%S')} UTC")
    