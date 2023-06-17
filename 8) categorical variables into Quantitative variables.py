# Turn categorical variables into Quantitaive variables

# import necessary libraries
import pandas as pd
import tkinter as tk
from tkinter import filedialog

# create a root
root = tk.Tk()
root.withdraw()

# Open file picker dialogue
file_path = filedialog.askopenfilename()

if file_path:

    # Load the data using pandas
    df = pd.read_excel(file_path,header=None)
    headers = df.iloc[0].tolist()
    df = df[1:]
    df.columns = headers
    print(df)

print(headers)
conversion_column = input("Enter the column to Turn categorical variables into Quantitaive variables: ")
A = pd.get_dummies(df[conversion_column])
df = pd.concat([df,A], axis=1)

print(df)

save_choice = input("Do you want to save file press Y or N: ")

if save_choice.lower() == "y":
    root.deiconify()
    root.lift()
    root.focus_force()

    save_path = tk.filedialog.asksaveasfilename(defaultextension='.xlsx')
    df.to_excel(save_path, index=False)
else:
    print("Ok.")










