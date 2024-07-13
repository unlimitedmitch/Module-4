# Load pre-installed packages
library(stats)
library(graphics)

# Data Cleaning
df <- read.csv('netflix_data.csv', stringsAsFactors = FALSE)

# Address missing values
print("Missing values before cleaning:")
print(colSums(is.na(df)))

# Fill missing values
df$director[is.na(df$director)] <- "Unknown"
df$cast[is.na(df$cast)] <- "Unknown"
df$country[is.na(df$country)] <- "Unknown"
df$rating[is.na(df$rating)] <- names(which.max(table(df$rating)))

# Handle 'duration' column
clean_duration <- function(row) {
  if (is.na(row['duration'])) {
    if (row['type'] == "Movie") {
      median_duration <- median(as.numeric(gsub(" min", "", df$duration[df$type == "Movie"])), na.rm = TRUE)
      return(paste(round(median_duration), "min"))
    } else {
      return(names(which.max(table(df$duration[df$type == "TV Show"]))))
    }
  }
  return(row['duration'])
}

df$duration <- apply(df, 1, clean_duration)

# Clean and convert 'date_added' column
df$date_added <- as.Date(df$date_added, format = "%B %d, %Y")
df$date_added[is.na(df$date_added)] <- median(df$date_added, na.rm = TRUE)

# Convert columns to appropriate data types
df$show_id <- as.character(df$show_id)
df$type <- as.factor(df$type)
df$release_year <- as.integer(df$release_year)
df$rating <- as.factor(df$rating)

print("Missing values after cleaning:")
print(colSums(is.na(df)))

# Data Exploration
print("Dataset Overview:")
str(df)

print("Numerical Data Summary:")
summary(df)

# Visualizations

# 1. Release Year Distribution
png("release_year_distribution.png", width = 800, height = 600)
hist(df$release_year, main = "Distribution of Release Years", xlab = "Release Year", col = "skyblue", border = "black")
dev.off()

# 2. Top 10 Directors by Number of Titles
director_counts <- sort(table(unlist(strsplit(df$director[df$director != "Unknown"], ", "))), decreasing = TRUE)[1:10]
png("top_directors.png", width = 800, height = 600)
barplot(director_counts, main = "Top 10 Directors by Number of Titles", horiz = TRUE, las = 1, col = "coral")
dev.off()

# 3. Content Type Distribution
png("content_type_distribution.png", width = 600, height = 600)
pie(table(df$type), main = "Distribution of Content Type", col = c("lightblue", "lightgreen"))
dev.off()

# 4. Ratings Distribution
png("ratings_distribution.png", width = 800, height = 600)
barplot(table(df$rating), main = "Distribution of Ratings", xlab = "Rating", ylab = "Count", col = "lightpink")
dev.off()

print("Data analysis and visualization complete. Check the generated PNG files for the visualizations.")