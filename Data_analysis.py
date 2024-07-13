import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data Cleaning
df = pd.read_csv('netflix_data.csv')

# Address missing values
print("Missing values before cleaning:")
print(df.isnull().sum())

# Fill missing values
df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Unknown', inplace=True)
df['country'].fillna('Unknown', inplace=True)
df['rating'].fillna(df['rating'].mode()[0], inplace=True)

# Handle 'duration' column separately for movies and TV shows
def clean_duration(row):
    if pd.isna(row['duration']):
        if row['type'] == 'Movie':
            return df[df['type'] == 'Movie']['duration'].str.extract('(\d+)').astype(float).median()[0].astype(int).astype(str) + ' min'
        else:
            return df[df['type'] == 'TV Show']['duration'].mode()[0]
    return row['duration']

df['duration'] = df.apply(clean_duration, axis=1)

# Clean and convert 'date_added' column
df['date_added'] = df['date_added'].str.strip()  # Remove leading/trailing whitespace
df['date_added'] = pd.to_datetime(df['date_added'], format='%B %d, %Y', errors='coerce')
df['date_added'].fillna(df['date_added'].mode()[0], inplace=True)

# Convert columns to appropriate data types
df['show_id'] = df['show_id'].astype('string')
df['type'] = df['type'].astype('category')
df['title'] = df['title'].astype('string')
df['director'] = df['director'].astype('string')
df['cast'] = df['cast'].astype('string')
df['country'] = df['country'].astype('string')
df['release_year'] = df['release_year'].astype('int')
df['rating'] = df['rating'].astype('category')
df['duration'] = df['duration'].astype('string')
df['listed_in'] = df['listed_in'].astype('string')
df['description'] = df['description'].astype('string')

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Data Exploration
print("\nDataset Overview:")
print(df.info())

print("\nNumerical Data Summary:")
print(df.describe())

# Data Visualization

# 1. Most watched genres
plt.figure(figsize=(12, 6))
genre_counts = df['listed_in'].str.split(', ', expand=True).stack().value_counts().head(10)
sns.barplot(x=genre_counts.index, y=genre_counts.values)
plt.title('Top 10 Most Watched Genres')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('top_genres.png')
plt.close()

# 2. Ratings distribution
plt.figure(figsize=(10, 6))
sns.countplot(x='rating', data=df, order=df['rating'].value_counts().index)
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('ratings_distribution.png')
plt.close()

# Additional visualizations

# 3. Content type distribution (Movie vs. TV Show)
plt.figure(figsize=(8, 6))
df['type'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribution of Content Type')
plt.ylabel('')
plt.savefig('content_type_distribution.png')
plt.close()

# 4. Top 10 countries producing content
plt.figure(figsize=(12, 6))
country_counts = df['country'].str.split(', ', expand=True).stack().value_counts().head(10)
sns.barplot(x=country_counts.index, y=country_counts.values)
plt.title('Top 10 Countries Producing Netflix Content')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('top_countries.png')
plt.close()

# 5. Content added over time
df['year_added'] = df['date_added'].dt.year
yearly_additions = df['year_added'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
yearly_additions.plot(kind='line', marker='o')
plt.title('Content Added to Netflix Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Titles Added')
plt.tight_layout()
plt.savefig('content_over_time.png')
plt.close()

print("Data analysis and visualization complete. Check the generated PNG files for the visualizations.")
