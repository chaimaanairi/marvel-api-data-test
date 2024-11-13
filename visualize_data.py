import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV with specified encoding
data = pd.read_csv("marvel_characters.csv", encoding='ISO-8859-1')

# Sort data by the number of comics in descending order and select the top 10 characters
top_characters = data.sort_values(by="Comic Count", ascending=False).head(10)

# Plot
plt.figure(figsize=(12, 8))
plt.barh(top_characters["Character Name"], top_characters["Comic Count"], color="skyblue")
plt.xlabel("Number of Comics")
plt.ylabel("Character Name")
plt.title("Top 10 Marvel Characters by Comic Appearances")
plt.gca().invert_yaxis()  # Reverse the order for better readability

# Show plot
plt.tight_layout()
plt.show()
