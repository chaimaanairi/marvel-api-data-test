import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV with specified encoding
data = pd.read_csv("marvel_characters.csv", encoding='ISO-8859-1')

# Sort data by the number of comics in descending order and select the top 10 characters
top_characters = data.sort_values(by="Comic Count", ascending=False).head(10)

# Plot
plt.figure(figsize=(12, 8))
plt.bar(top_characters["Character Name"], top_characters["Comic Count"], color="skyblue")
plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for better readability
plt.xlabel("Character Name")         # x-axis label
plt.ylabel("Comic Count")            # y-axis label
plt.title("Top 10 Marvel Characters by Comic Appearances")

# Show plot
plt.tight_layout()
plt.show()
