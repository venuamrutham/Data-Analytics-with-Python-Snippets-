
# code To read a excel file and showing the headers 

import tkinter as tk
from tkinter import filedialog
import pandas as pd

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Open the file picker dialog
file_path = filedialog.askopenfilename()

# Check if a file was selected
if file_path:
    # Load the data using Pandas
    df = pd.read_csv(file_path, header=None)  # Specify that the file has no headers

    # Get the headers
    headers = df.iloc[0].tolist()

    # Update the DataFrame with the correct headers
    df = df[1:]  # Remove the first row (headers row)
    df.columns = headers  # Assign the retrieved headers to the DataFrame columns

    # Display the headers
    print(headers)

    # Print the data frame
    print(df)
