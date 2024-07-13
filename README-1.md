# Netflix Data Analysis Project

This project analyzes Netflix content data using both Python and R. The analysis includes data cleaning, exploration, and visualization to gain insights into Netflix's content library.

## Python Script

The Python script (`Data_analysis.py`) performs the following tasks:

1. Data Cleaning:
   - Loads data from 'netflix_data.csv'
   - Handles missing values in various columns
   - Cleans and converts the 'date_added' column to datetime format
   - Converts all columns to appropriate data types

2. Data Exploration:
   - Provides an overview of the dataset structure
   - Generates summary statistics for numerical data

3. Data Visualization:
   - Creates five visualizations:
     a. Top 10 Most Watched Genres
     b. Distribution of Ratings
     c. Distribution of Content Type (Movie vs. TV Show)
     d. Top 10 Countries Producing Netflix Content
     e. Content Added to Netflix Over Time

The visualizations are saved as PNG files in the same directory as the script.

## R Script

The R script performs similar data cleaning and exploration tasks as the Python script, but creates different visualizations:

1. Data Cleaning:
   - Loads data from 'netflix_data.csv'
   - Handles missing values
   - Cleans the 'date_added' and 'duration' columns
   - Converts columns to appropriate data types

2. Data Exploration:
   - Provides an overview of the dataset structure
   - Generates summary statistics

3. Data Visualization:
   - Creates four new visualizations:
     a. Distribution of Release Years
     b. Top 10 Directors by Number of Titles
     c. Content Type Distribution
     d. Ratings Distribution

The R script uses base R functions to ensure compatibility across different R environments.

## Requirements

- Python: pandas, matplotlib, seaborn
- R: Base R (no additional packages required)

## Usage

1. Ensure 'netflix_data.csv' is in the same directory as the scripts.
2. Run the Python script: `python Data_analysis.py`
3. Run the R script in an R environment

The scripts will generate PNG files with the visualizations in the same directory.