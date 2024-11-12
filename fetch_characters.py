import requests
import hashlib
import time

# Your API keys
public_key = '25dc2a8ba6477fd6faf4788a1d51f4f2'
private_key = 'b7c49faadee8c8a9054ff34b2839ba9fddd2edeb'

# Generate hash
timestamp = str(int(time.time()))
hash_value = hashlib.md5(f"{timestamp}{private_key}{public_key}".encode('utf-8')).hexdigest()

# Marvel API endpoint for characters
url = "https://gateway.marvel.com/v1/public/characters"

# Parameters for the API request
params = {
    'ts': timestamp,
    'apikey': public_key,
    'hash': hash_value
}

# Make the request to the Marvel API
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    # Process and print character names and the number of comics they appear in
    for character in data['data']['results']:
        character_name = character['name']
        comics_count = len(character['comics']['items'])
        print(f"Character: {character_name}, Appears in {comics_count} comics")
else:
    print(f"Failed to retrieve data: {response.status_code}")
