import pandas as pd

# Load the CSV file into a DataFrame without assuming headers
df = pd.read_csv('AStrocsv1.csv', header=None)

# Display column names and the first few rows to confirm the structure
print("Initial DataFrame structure:\n", df.head())

# Check the number of columns
print("Number of columns in the DataFrame:", len(df.columns))

# If there are only 3 columns, assume the structure and correct the naming
if len(df.columns) == 3:
    df.columns = ['DateTime', 'SaturnLong', 'Long']  # Assuming 'DateTime' as combined Date and Time

    # Split 'DateTime' into separate 'Date' and 'Time' columns
    df[['Date', 'Time']] = df['DateTime'].str.split(' ', expand=True)

    # Convert 'SaturnLong' and 'Long' columns to float
    df['SaturnLong'] = df['SaturnLong'].astype(float)
    df['Long'] = df['Long'].astype(float)

    # Calculate the difference between 'SaturnLong' and 'Long' and store in 'result' column
    df['result'] = df['SaturnLong'] - df['Long']

    # Check for rows where the result is 30 and store the corresponding dates and times
    matching_rows = df[df['result'].round(6) == 30.0][['Date', 'Time']]

    # Print the matching dates and times
    print("Dates and times where the result is 30:")
    print(matching_rows)
else:
    print("The CSV file does not have the expected number of columns (3). Please check the file structure.")
