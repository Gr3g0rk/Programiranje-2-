import simplejson as json
import pandas as pd
import csv
file_name = "DrugSeizures.xlsx"
xl_file = pd.ExcelFile(file_name)
dfs = {sheet_name: xl_file.parse(sheet_name) 
          for sheet_name in xl_file.sheet_names}
data = dfs['Seizures']
fullJson = {"data" : []}


for index, row in data[3:-1].iterrows():
# each row is returned as a pandas series
    fullJson["data"].append({
        "Region" : row["Drug seizures 2015-2019"],
        "Country" : row["Unnamed: 2"],
        "Year" : row["Unnamed: 4"],
        "DrugGroup" : row["Unnamed: 5"],
        "Drug" : row["Unnamed: 6"],
        "Kilograms" : row["Unnamed: 10"],
        "Code" : row["Unnamed: 13"]
    })

with open("C:\\Projects\\Droge\\DrugSeizures.json", "w") as outfile:
    json.dump(fullJson, outfile, ignore_nan=True)