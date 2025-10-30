import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("netflix_titles.csv")

# # ========== CHECK FOR MISSING VALUES ==========
print("=== Missing Values in Each Column ===\n")
print(df.isnull().sum(), "\n")

# # ========== DROP MISSING VALUES ==========
print("=== Dropping Rows with Missing 'country', 'director', or 'release_year' ===\n")
df.dropna(subset=['country', 'director', 'release_year'], inplace=True)
print("Rows after dropping missing values:", len(df), "\n")

# # ========== TYPE COUNT ==========
print("=== Count of Each Type (Movie/TV Show) ===\n")
print(df['type'].value_counts(), "\n")

# # ========== COUNTRY WITH MAX CONTENT ==========
print("=== Country with Maximum Content ===\n")
max_content = df['country'].value_counts().idxmax()
value = df['country'].value_counts().max()
print(f"{max_content}: {value}\n")

# # ========== MOST FREQUENT GENRE ==========
print("=== Most Frequent Genre/Category (from 'listed_in') ===\n")
print(df['listed_in'].mode()[0], "\n")

# ========== TREND OF TITLES RELEASED EACH YEAR ==========
print("=== Trend of Number of Netflix Titles Released Each Year ===\n")
trend = df['release_year'].value_counts().sort_index()

plt.figure(figsize=(8,5))
plt.plot(trend.index, trend.values, marker='o')
plt.title('Number of Netflix Titles Released Each Year',fontweight='bold')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')
plt.tight_layout()
plt.show()

# ========== TOP 10 COUNTRIES WITH MOST TITLES ==========
print("=== Top 10 Countries with the Most Netflix Titles ===\n")
top_countries = df['country'].value_counts().head(10)
print(top_countries, "\n")

plt.figure(figsize=(10,5))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='coolwarm')
plt.title("Top 10 Countries by Number of Netflix Titles",fontweight='bold')
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.show()