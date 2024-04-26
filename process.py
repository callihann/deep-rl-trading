import os
import pandas as pd

# Function to read CSV files, transpose, and return DataFrame without header
def process_csv(file_path):
    df = pd.read_csv(file_path, header=None)
    transposed_df = df.transpose()
    # Drop header
    transposed_df = transposed_df.iloc[1:]
    return transposed_df

# Path to the folder containing CSV files
for i in range(1, 11):
    folder_path = f'Figures/Block {i}'
    # List to store DataFrames from all CSV files
    dfs = []

    # Iterate over files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            # Process each CSV file and append to the list
            dfs.append(process_csv(file_path))

    # Combine all DataFrames into a single DataFrame
    combined_df = pd.concat(dfs, ignore_index=True)

    # Save the combined DataFrame to a new CSV file
    combined_df.to_csv(f'Block {i}.csv', index=False)
