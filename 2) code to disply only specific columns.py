# code to disply only specific columns

import tkinter as tk
from tkinter import filedialog
import pandas as pd

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

if file_path:
    df = pd.read_csv(file_path, header=None)

    headers = df.iloc[0].tolist()

    df = df[1:]
    df.columns = headers

    print(headers)

specific_columns = ["make","price"]

print(df[specific_columns])




