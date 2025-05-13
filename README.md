# Data Analysis Script README

This script performs basic data analysis on a dataset, assumed to contain information about students' habits and performance. It utilizes the pandas, NumPy, Matplotlib, and Seaborn libraries for data manipulation, numerical operations, and visualization.

## Prerequisites

Before running the script, ensure you have the following Python libraries installed:

-   pandas (`pip install pandas`)
-   NumPy (`pip install numpy`)
-   Matplotlib (`pip install matplotlib`)
-   Seaborn (`pip install seaborn`)

Additionally, the script expects a CSV file named `students.csv` to be present in the same directory as the script.

## Functionality

The script performs the following actions:

1.  **Imports Libraries:** Imports the necessary libraries: `pandas` for data manipulation, `numpy` for numerical operations, `matplotlib.pyplot` for basic plotting, and `seaborn` for enhanced visualizations.

2.  **Error Handling:** Attempts to read the `students.csv` file. If the file is not found, it prints an error message and exits.

3.  **Data Exploration:**
    -   Displays the first 5 rows of the dataset using `df.head()`.
    -   Prints a summary of the dataset's structure, including data types and non-null values, using `df.info()`.
    -   Checks for and prints the number of missing values in each column using `df.isnull().sum()`.

4.  **Data Cleaning:**
    -   Removes rows with any missing values using `df.dropna()`.
    -   Removes duplicate rows using `df.drop_duplicates()`.

5.  **Descriptive Statistics:**
    -   Calculates and prints descriptive statistics (count, mean, standard deviation, min, max, quartiles) for the numerical columns in the cleaned DataFrame using `df.describe()`.

6.  **Grouped Analysis:**
    -   Calculates and prints the mean of the `study_hours_per_day` column, grouped by the `age` column.
    -   Includes a check to ensure that the `age` and `study_hours_per_day` columns exist in the DataFrame. If not, it prompts the user to update the column names.

7.  **Data Visualization:**
    -   **Line Chart:** Generates a line chart showing the average exam score for each age group.
        -   Calculates the mean exam score grouped by age.
        -   Uses `matplotlib.pyplot` to create and display the line chart with appropriate labels and title.
    -   **Bar Chart:** Generates a bar chart showing the average `study_hours_per_day` for each `age`.
        -   Uses `seaborn.barplot` for creating the bar chart.
        -   Includes a title and rotates x-axis labels for better readability.
    -   **Histogram:** Generates a histogram showing the distribution of `study_hours_per_day`.
        -   Uses `seaborn.histplot` to create the histogram with 20 bins and a Kernel Density Estimate (KDE) curve.
        -   Includes a title and axis labels.
    -   **Scatter Plot:** Generates a scatter plot to visualize the relationship between 'Sales' and 'Profit'.
        -   Includes a check to ensure that the 'Sales' and 'Profit' columns exist in the DataFrame. If not, it prompts the user to update the column names to match numeric columns in their dataset.
        -   Uses `seaborn.scatterplot` to create the scatter plot, with the 'Sales' column used for both x-axis and color hue.
        -   Includes a title, axis labels, and a legend.

## How to Run the Script

1.  Save the provided Python code as a `.py` file (e.g., `data_analysis.py`).
2.  Ensure that the `students.csv` file is in the same directory as the Python script.
3.  Open a terminal or command prompt, navigate to the directory where you saved the files, and run the script using the command: `python data_analysis.py`

The script will print the initial rows, dataset information, missing values, descriptive statistics, and the grouped mean of study hours. It will also display the generated line chart, bar chart, histogram, and scatter plot.
