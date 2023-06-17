# Binning

# import necessary libraries
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askdirectory

# Create root
root = tk.Tk()
root.withdraw()

# Open file picker dialog
file_path = filedialog.askopenfilename()

if file_path:

    # Load data using pandas
    df = pd.read_excel(file_path)
    print(df.columns)

    column_for_binning = input("Enter the column header to perform binning: ")

    # Convert the column to numeric if not already
    if not pd.api.types.is_numeric_dtype(df[column_for_binning]):
        df[column_for_binning] = pd.to_numeric(df[column_for_binning], errors='coerce')

    bin_labels = ['Low', 'Medium', 'High', 'Very High']
    bin_edges = pd.cut(df[column_for_binning], bins=4, labels=bin_labels)
    df['binned_data'] = bin_edges

print(df)

root.deiconify()
root.lift()
root.focus_force()

save_path = tk.filedialog.asksaveasfilename(defaultextension='.xlsx')
df.to_excel(save_path, index=False)

