from datetime import datetime, timezone
import time
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
    

def get_iss_position():
    data = fetch_iss_data()
    if data is None:
        return None
    
    return parse_position(data) 


def collect_positions(count,delay):
    history = []
    for a in range(count):
        result = get_iss_position()
        if result is not None:
            history.append(result)
        time.sleep(delay)

    return history

history = collect_positions(5,5)
for lat,lon,when in history:
    print(f"{lat:.2f}, {lon:.2f} at {when.strftime('%H:%M:%S')} UTC")
print(f"Collected {len(history)} positions.")
