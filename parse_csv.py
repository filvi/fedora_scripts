import os
import pandas as pd
from sys import argv
import json

# initializing variables
mypath    = ""
output    = ""
read_json = ""




help_msg = """
Filter data from CSV giving names in JSON files
Switches:

-i  \tinput filepath 
-o \toutput filepath
-r \tjson path to pick the filter
-c \tname of the colum [m]oodle VS [z]oom

"""
for i in range(1, len(argv)):
    if argv[i] == "-i":
        mypath = argv[i + 1]
    if argv[i] == "-o":
        output = argv[i + 1]
    if argv[i] == "-r":
        read_json = argv[i + 1]
    if argv[i] == "-c":
        if argv[i + 1].lower() == "m":
            column = "Nome completo dell'utente"
        if argv[i + 1].lower() == "z":
            column = "Name (Original Name)"
    if argv[i] == "-h" or argv[i] == "--help":
        print(help_msg)
        exit()
        
    
if mypath == "":
    mypath = input("Insert path of CSV file: ")
if output == "":
    output = input("Insert the output filename: ")
if read_json == "":
    read_json = input("Insert the path to json file: ")
if column == "":
    column = input("Insert the Column of the CSV file: ")


if not output.endswith(".csv"):
    output += ".csv"

with open(read_json) as u:
    lista = json.load(u)
print("\n\nUsers found in file JSON: \n- " + "\n- ".join(lista))


for root, dirs, files in os.walk(mypath):
    for f in files:
        fname, ext = os.path.splitext(f)
        if ext == ".csv":
            print(f"\n\nCSV found: {fname}{ext}")
            csv_file = os.path.join(root,f"{fname}{ext}")
            df = pd.read_csv(csv_file)
            temp =  df[column].str.lower().isin([x.lower() for x in lista])
            ret = df[temp]
            ret.to_csv(rf'{output}', index=False)
            destination = os.path.join(mypath, output)
            os.replace(output, destination)
            print(f"File {output}, written")
            # os.system(f"nautilus {mypath}")

            
        