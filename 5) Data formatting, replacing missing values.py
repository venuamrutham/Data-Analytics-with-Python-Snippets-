# Data formatting, replacing missing values, coverting

# import necessary libraries
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import numpy as np

# Create a root
root = tk.Tk()
root.withdraw()

# Open filepicker dialog
file_path = filedialog.askopenfilename()

if file_path:
    # Load data using pandas
    df = pd.read_excel(file_path, header=None)

    # Get the headers
    headers = df.iloc[0].tolist()
    df = df[1:]
    df.columns = headers

print(df)

df['marks'] = pd.to_numeric(df['marks'], errors='coerce')     # Coverts the data into int type

mean = df["marks"].mean()                                     # Finding mean

df["marks"].replace(np.nan,mean,inplace=True)                 # Filling mean in Nan place, df["marks"].fillna(mean, inplace=True) also gives same result

df.rename(columns = {"marks":"Updated_marks"}, inplace=True)  # Renaming the column

print(df)






