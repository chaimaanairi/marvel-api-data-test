import requests
import ssl
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager  # Fixed import for PoolManager

# Custom adapter to adjust SSL settings for requests
class TLSAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = ssl.create_default_context()
        # Set the ciphers to allow less secure ciphers (use only if necessary)
        context.set_ciphers('DEFAULT@SECLEVEL=1')
        kwargs['ssl_context'] = context
        return super().init_poolmanager(*args, **kwargs)


# URL and parameters for the Marvel API request
url = "https://gateway.marvel.com/v1/public/characters"
params = {
    'ts': '1731450075',
    'apikey': '25dc2a8ba6477fd6faf4788a1d51f4f2',
    'hash': '7ebc04237cc5e7ceaf4c9bdafa9a9539'
}
headers = {
    'User-Agent': 'Mozilla/5.0'
}

# Create a session to reuse the TLSAdapter settings for multiple requests
session = requests.Session()
session.mount('https://', TLSAdapter())  # Use custom adapter for HTTPS requests

# Make the GET request and handle possible errors
try:
    # Send the GET request with parameters and headers
    response = session.get(url, params=params, headers=headers)
    response.raise_for_status()  # Raises an HTTPError for bad HTTP responses (4xx and 5xx)

    # If the request was successful, print the JSON response
    print(response.json())

except requests.exceptions.SSLError as e:
    print(f"SSL Error encountered: {e}")
except requests.exceptions.RequestException as e:
    print(f"HTTP Error encountered: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
