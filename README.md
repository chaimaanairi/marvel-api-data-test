# Marvel API Data Visualization

This project fetches data from the Marvel API, processes it, and visualizes information about Marvel characters, including how many comics each character appears in.

## Overview

The project uses the **Marvel API** to gather data on Marvel characters and the number of comics they appear in. The process involves:
1. **Generating a secure hash** for authentication to access the Marvel API.
2. **Fetching the character data** from the Marvel API and storing it in a CSV file.
3. **Visualizing** the characters and the number of comics they appear in using bar charts.

## Project Structure

- `generate_hash.py`: Generates the required hash and timestamp for API authentication.
- `fetch_characters.py`: Fetches character data (names and comic counts) from the Marvel API, sorted alphabetically by character name, and saves it to a CSV file.
- `visualize_data.py`: Reads the CSV file and visualizes the data with a bar chart using `matplotlib`.
- `marvel_characters.csv`: The output CSV file containing the character names and comic counts.

## Requirements

To set up and run this project, you will need:
- Python 3.x  (I am using Python 3.10.8)
- An API key from Marvel's Developer Portal: [https://developer.marvel.com](https://developer.marvel.com)
- Python packages: `requests`, `pandas`, `matplotlib`

Install the necessary packages using:
```bash
pip install requests pandas matplotlib
```

## Setup and Usage

### 1. Marvel API Authentication
Get a **public key** and **private key** from the [Marvel Developer Portal](https://developer.marvel.com/) to get your API keys. 
Update the `public_key` and `private_key` in `generate_hash.py` with your keys.

### 2. Generate Hash
Run `generate_hash.py` to create the hash value used for authentication in Marvel API requests.
```bash
python generate_hash.py
```

### 3. Fetch Character Data
Run `fetch_characters.py` to retrieve character names and comic counts from the Marvel API, sorted alphabetically by character name, and save them to `marvel_characters.csv`.
```bash
python fetch_characters.py
```
This script will save character names and their comic appearance counts to a CSV file, allowing for further analysis.

### 4. Visualize Data
Run `visualize_data.py` to load the CSV data and visualize the top 10 characters by their number of comic appearances in a bar chart.
```bash
python visualize_data.py
```
This script will display a bar chart with the character names on the x-axis and their comic counts on the y-axis.


## Visualization Example
The `visualize_data.py` script generates a bar chart like the example below:
- **X-axis**: Character Names
- **Y-axis**: Comic Count

![Data_Visualization_ Bar_chart.png](Data_Visualization_%20Bar_chart.png)

This provides a quick view of which Marvel characters appear in the most comics, highlighting the popularity of top characters.

