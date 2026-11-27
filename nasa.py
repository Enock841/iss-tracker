import requests
URL = "https://api.nasa.gov/planetary/apod"


def fetch_apod():
    try:
        response = requests.get(URL,params={"api_key":"DEMO_KEY"},timeout = 5)
        response.raise_for_status()
        data = response.json()
        return data
    
    except requests.RequestException as e:
        print(f"Could not fetch NASA image: {e}")
        return None


if __name__ == "__main__":
    print(fetch_apod())