import os
import requests
import ssl
import csv
from requests.adapters import HTTPAdapter
from generate_hash import generate_hash  # Import the hash generation function


# Custom adapter to adjust SSL settings for requests
class TLSAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = ssl.create_default_context()
        context.set_ciphers('DEFAULT@SECLEVEL=1')
        kwargs['ssl_context'] = context
        return super().init_poolmanager(*args, **kwargs)


# Marvel API details
public_key = '25dc2a8ba6477fd6faf4788a1d51f4f2'  # Replace with actual key or load from environment
url = "https://gateway.marvel.com/v1/public/characters"

# Generate timestamp and hash
ts, hash_value = generate_hash()


# Function to fetch Marvel character data
def fetch_character_data(limit=100):
    params = {
        'ts': ts,
        'apikey': public_key,
        'hash': hash_value,
        'limit': limit
    }
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Create a session to reuse TLSAdapter settings for HTTPS requests
    session = requests.Session()
    session.mount('https://', TLSAdapter())

    try:
        response = session.get(url, params=params, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        return response.json()

    except requests.exceptions.SSLError as e:
        print(f"SSL Error encountered: {e}")
    except requests.exceptions.RequestException as e:
        print(f"HTTP Error encountered: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None


# Function to save data to CSV
def save_data_to_csv(data, filename='marvel_characters.csv'):
    characters = data['data']['results']

    # Sort characters by name
    sorted_characters = sorted(characters, key=lambda x: x['name'])

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Character Name', 'Comic Count'])

        for character in sorted_characters:
            name = character['name']
            comics_count = character['comics']['available']
            writer.writerow([name, comics_count])

    print(f"Data saved to {filename}")


# Main script execution
if __name__ == "__main__":
    data = fetch_character_data()
    if data:
        save_data_to_csv(data)
