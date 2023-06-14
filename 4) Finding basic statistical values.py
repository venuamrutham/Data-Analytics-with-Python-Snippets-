# Finding basic statistical values

# import necessary libraries
import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Create a root
root = tk.Tk()

# Withdraw root
root.withdraw

# Open filepicker dialogue
file_path = filedialog.askopenfilename()

if file_path:
    # Load data using pandas
    df = pd.read_excel(file_path,header=None)

    # Get the headers
    headers = df.iloc[0].tolist()

    df.columns = headers

print(df)

print(headers)

df['marks'] = pd.to_numeric(df['marks'], errors='coerce')

# Calculate the mean of a specific column
mean_value1 = df['marks'].mean()

print(mean_value1)

# Calculate statistics for a specific column
column_stats = df['marks'].describe()
print(column_stats)





