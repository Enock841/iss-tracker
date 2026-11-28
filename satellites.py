import requests
URL = "https://celestrak.org/NORAD/elements/gp.php"


def fetch_tle(catnr):
    try:
        response = requests.get(URL,params={"CATNR":catnr,"FORMAT":"TLE"}, timeout=5)
        response.raise_for_status()
        data = response.text
        return data
    
    except requests.RequestException as e:
        print(f"Could not fetch orbit: {e}")
        return None


if __name__ == "__main__":
    print(fetch_tle(25544))