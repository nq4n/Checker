import requests
import time
from datetime import datetime

URL = "https://muaiyad.onrender.com/"

while True:
    try:
        response = requests.get(URL, timeout=30)

        print(
            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
            f"Site opened successfully | Status: {response.status_code}"
        )

    except Exception as e:
        print(
            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
            f"Error: {e}"
        )

    # wait 1 hour
    time.sleep(3600)
