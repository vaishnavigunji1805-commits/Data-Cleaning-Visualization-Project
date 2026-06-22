
# Netflix Data Cleaning & Visualization Project


# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Load Dataset

df_netflix = pd.read_csv('/content/netflix_titles.csv.zip')

print("Dataset Shape:", df_netflix.shape)
display(df_netflix.head())


# Check Missing Values

print("\nMissing Values:")
print(df_netflix.isnull().sum())


# Handle Missing Values

df_netflix['director'] = df_netflix['director'].fillna('Unknown')
df_netflix['cast'] = df_netflix['cast'].fillna('Unknown')
df_netflix['country'] = df_netflix['country'].fillna('Unknown')

# Fill rating with most frequent value
df_netflix['rating'] = df_netflix['rating'].fillna(
    df_netflix['rating'].mode()[0]
)


# Remove Duplicate Records

duplicates_before = df_netflix.duplicated().sum()

df_netflix.drop_duplicates(inplace=True)

duplicates_after = df_netflix.duplicated().sum()

print("\nDuplicates Removed:", duplicates_before)
print("Remaining Duplicates:", duplicates_after)

# Summary Statistics

print("\nSummary Statistics:")
print(df_netflix.describe())


# Missing Values Heatmap

plt.figure(figsize=(10, 5))
sns.heatmap(df_netflix.isnull(), yticklabels=False, cbar=True)
plt.title("Missing Values Heatmap")
plt.show()


# Release Year Distribution

plt.figure(figsize=(10, 5))
sns.histplot(df_netflix['release_year'], bins=30)
plt.title("Release Year Distribution")
plt.xlabel("Release Year")
plt.ylabel("Frequency")
plt.show()


# Release Year Boxplot

plt.figure(figsize=(8, 4))
sns.boxplot(x=df_netflix['release_year'])
plt.title("Release Year Boxplot")
plt.show()


# Movies vs TV Shows

plt.figure(figsize=(6, 4))
sns.countplot(data=df_netflix, x='type')
plt.title("Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Count")
plt.show()


# Top 10 Countries Producing Content

top_countries = (
    df_netflix['country']
    .value_counts()
    .head(10)
)

plt.figure(figsize=(10, 5))
top_countries.plot(kind='bar')
plt.title("Top 10 Content Producing Countries")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.show()


# Content Rating Distribution

plt.figure(figsize=(10, 6))
sns.countplot(
    data=df_netflix,
    y='rating',
    order=df_netflix['rating'].value_counts().index
)

plt.title("Content Rating Distribution")
plt.xlabel("Count")
plt.ylabel("Rating")
plt.show()


# Content Added Over Time

df_netflix['date_added'] = pd.to_datetime(
    df_netflix['date_added'],
    errors='coerce'
)

content_by_year = (
    df_netflix['date_added']
    .dt.year
    .value_counts()
    .sort_index()
)

plt.figure(figsize=(10, 5))
content_by_year.plot()
plt.title("Netflix Content Added by Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles Added")
plt.grid(True)
plt.show()


# Final Dataset Information

print("\nFinal Dataset Shape:", df_netflix.shape)
print("\nDataset Information:")
print(df_netflix.info())
