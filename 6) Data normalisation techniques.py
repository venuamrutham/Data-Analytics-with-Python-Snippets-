# Data normalisation techniques

# importing necessary libraries
import pandas as pd
import tkinter as tk
from tkinter import filedialog

# creating root
root = tk.Tk()
root.withdraw()

# Open filepicker dialogue
file_path = filedialog.askopenfilename()

if file_path:
    # Load data using pandas
    df = pd.read_excel(file_path,header=None)

    # Get the headers
    headers = df.iloc[0].tolist()

    df = df[1:]
    df.columns = headers

print("The file before normalisation\n", df)

type_of_normalisation = int(input("Press 1 for Simple scaling, Press 2 for Min-Max, press 3 for Z-score: "))

if type_of_normalisation == 1:
    print("Columns available for Simple scaling Normalisation technique: ")
    print(df.columns)
    column_choices = input("Enter the column headers to normalize (CASE SENSITIVE), separated by commas: ")
    column_choices = [col.strip() for col in column_choices.split(",")]

    for column_choice in column_choices:
        if column_choice in headers:
            df[column_choice] = pd.to_numeric(df[column_choice], errors='coerce')
            Simple_scaled_column = df[column_choice] / df[column_choice].max()
            df[column_choice] = Simple_scaled_column
        else:
            print(f"Column '{column_choice}' not found")

    print(df)

elif type_of_normalisation == 2:

    print("Columns available for Min-Max Normalisation technique: ")
    print(df.columns)
    column_choices = input("Enter the column headers to normalize (CASE SENSITIVE), separated by commas: ")
    column_choices = [col.strip() for col in column_choices.split(",")]

    for column_choice in column_choices:
        if column_choice in headers:
            df[column_choice] = pd.to_numeric(df[column_choice], errors='coerce')
            Min_Max_column = (df[column_choice]-df[column_choice].min())/(df[column_choice].max()-df[column_choice].min())
            df[column_choice] = Min_Max_column
        else:
            print(f"Column '{column_choice}' not found")

    print(df)
    

elif type_of_normalisation == 3:
    
    print("Columns available for Z-score Normalisation technique: ")
    print(df.columns)
    column_choices = input("Enter the column headers to normalize (CASE SENSITIVE), separated by commas: ")
    column_choices = [col.strip() for col in column_choices.split(",")]

    for column_choice in column_choices:
        if column_choice in headers:
            df[column_choice] = pd.to_numeric(df[column_choice], errors='coerce')
            Z_score_column = (df[column_choice]-df[column_choice].mean())/df[column_choice].std()
            df[column_choice] = Z_score_column
        else:
            print(f"Column '{column_choice}' not found")

    print(df)

else:

    print("Not a valid entry, run again .......")
    





