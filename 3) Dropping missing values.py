# Dropping missing values

# import necessary libraries

import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Create a tkinter root
root = tk.Tk()

# Withdraw root
root.withdraw

# Open filepicker dialog
file_path = filedialog.askopenfilename()

if file_path:
    #load data using pandas
    df = pd.read_excel(file_path, header=None)

    # Get the headers
    headers = df.iloc[0].tolist()

    # Update the dataframe with correct headers
    df = df[1:]
    df.columns = headers

# To print data frame
print(df)

# To print headers
print(headers)

# Dropping rows with any missing values
df = df.dropna(subset=['marks'], inplace=False)

print(df)













