# Marvel API Data Visualization

This project fetches data from the Marvel API, processes it, and visualizes information about Marvel characters, including how many comics each character appears in.

## Overview

The project uses the **Marvel API** to gather data on Marvel characters and the number of comics they appear in. The process involves:
1. **Generating a secure hash** for authentication to access the Marvel API.
2. **Fetching the character data** from the Marvel API and storing it in a CSV file.
3. **Visualizing** the characters and the number of comics they appear in using bar charts.

## Project Structure

- `generate_hash.py`: Generates the required hash and timestamp for API authentication.
- `fetch_characters.py`: Fetches character data (names and comic counts) from the Marvel API and saves it to a CSV file.
- `visualize_data.py`: Reads the CSV file and visualizes the data with a bar chart using `matplotlib`.
- `marvel_characters.csv`: The output CSV file containing the character names and comic counts.

