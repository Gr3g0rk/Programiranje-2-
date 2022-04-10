import requests as rq
import simplejson as json
import csv
import pandas as pd
import matplotlib.pyplot as plt
from turtle import color
import numpy as np

file_name = "Overdose.xlsx"
xl_file = pd.ExcelFile(file_name)

dfs = {sheet_name: xl_file.parse(sheet_name) 
          for sheet_name in xl_file.sheet_names}
drugOdDeathsData = dfs["Number Drug OD Deaths"][5:]
def readrow(datframe, datfkeys, nrow = 0):
    row = []
    for el in datfkeys:
        row.append(datframe.iloc[nrow][el])
    return row
years = readrow(drugOdDeathsData, drugOdDeathsData.iloc[0].keys()[2:-2])

drugOdDeathsData = drugOdDeathsData[2:]
total_maleODDeaths = readrow(drugOdDeathsData, drugOdDeathsData.iloc[1].keys()[2:-2], 1)
total_femaleODDeaths = readrow(drugOdDeathsData, drugOdDeathsData.iloc[0].keys()[2:-2], 0)

opioid_maleODDeaths = readrow(drugOdDeathsData, drugOdDeathsData.iloc[4].keys()[2:-2], 4)
opioid_femaleODDeaths = readrow(drugOdDeathsData, drugOdDeathsData.iloc[3].keys()[2:-2], 3)

heroin_maleODDeaths = readrow(drugOdDeathsData, drugOdDeathsData.iloc[20].keys()[2:-2], 20)
heroin_femaleODDeaths = readrow(drugOdDeathsData, drugOdDeathsData.iloc[19].keys()[2:-2], 19)

cocaine_maleODDeaths = readrow(drugOdDeathsData, drugOdDeathsData.iloc[29].keys()[2:-2], 29)
cocaine_femaleODDeaths = readrow(drugOdDeathsData, drugOdDeathsData.iloc[28].keys()[2:-2], 28)

benzodiazepines_maleODDeaths = readrow(drugOdDeathsData, drugOdDeathsData.iloc[59].keys()[2:-2], 59)
benzodiazepines_femaleODDeaths = readrow(drugOdDeathsData, drugOdDeathsData.iloc[58].keys()[2:-2], 58)

antidepressants_maleODDeaths = readrow(drugOdDeathsData, drugOdDeathsData.iloc[74].keys()[2:-2], 74)
antidepressants_femaleODDeaths = readrow(drugOdDeathsData, drugOdDeathsData.iloc[73].keys()[2:-2], 73)

newJson = {
    "m_deaths" : total_maleODDeaths,
    "f_deaths" : total_femaleODDeaths,
    "m_opioid" : opioid_maleODDeaths,
    "f_opioid" : opioid_femaleODDeaths,
    "m_heroin" : heroin_maleODDeaths,
    "f_heroin" : heroin_femaleODDeaths,
    "m_cocaine" : cocaine_maleODDeaths,
    "f_cocaine" : cocaine_femaleODDeaths,
    "m_benzodiazepines" : benzodiazepines_maleODDeaths,
    "f_benzodiazepines" : benzodiazepines_femaleODDeaths,
    "m_antidepressants" : antidepressants_maleODDeaths,
    "f_antidepressants" : antidepressants_femaleODDeaths
}
with open("OverDose.json", "w") as outfile:
    json.dump(newJson, outfile, ignore_nan=True)

def graf_antidepresivi():
    labels = years
    men_means = antidepressants_maleODDeaths
    women_means = antidepressants_femaleODDeaths

    x = np.arange(len(labels))  
    width = 0.35  

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, men_means, width, label='Moški')
    rects2 = ax.bar(x + width/2, women_means, width, label='Ženske', color = 'pink')

   
    ax.set_xlabel('Leta')
    ax.set_ylabel('Št. overdosov')
    ax.set_title('Overdosi zaradi antidepresivov')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()
    plt.show()

def graf_benzodiazepines():
    labels = years
    men_means = benzodiazepines_maleODDeaths
    women_means = benzodiazepines_femaleODDeaths

    x = np.arange(len(labels))  
    width = 0.35  

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, men_means, width, label='Moški')
    rects2 = ax.bar(x + width/2, women_means, width, label='Ženske', color = 'pink')

    
    ax.set_xlabel('Leta')
    ax.set_ylabel('Št. overdosov')
    ax.set_title('Overdosi zaradi benzodiazepinov')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()

def graf_kokain():
    labels = years
    men_means = cocaine_maleODDeaths
    women_means = cocaine_femaleODDeaths

    x = np.arange(len(labels))  
    width = 0.35  

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, men_means, width, label='Moški')
    rects2 = ax.bar(x + width/2, women_means, width, label='Ženske', color = 'pink')

    
    ax.set_xlabel('Leta')
    ax.set_ylabel('Št. overdosov')
    ax.set_title('Overdosi zaradi kokaina')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()

def graf_heroin():
    labels = years
    men_means = heroin_maleODDeaths
    women_means = heroin_femaleODDeaths

    x = np.arange(len(labels))
    width = 0.35  

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, men_means, width, label='Moški')
    rects2 = ax.bar(x + width/2, women_means, width, label='Ženske', color = 'pink')

    ax.set_xlabel('Leta')
    ax.set_ylabel('Št. overdosov')
    ax.set_title('Overdosi zaradi heroina')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()

def graf_opiods():
    labels = years
    men_means = opioid_maleODDeaths
    women_means = opioid_femaleODDeaths

    x = np.arange(len(labels)) 
    width = 0.35 

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, men_means, width, label='Moški')
    rects2 = ax.bar(x + width/2, women_means, width, label='Ženske', color = 'pink')

    ax.set_xlabel('Leta')
    ax.set_ylabel('Št. overdosov')
    ax.set_title('Overdosi zaradi opioidov')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()

def graf_skupni():

    labels = years
    men_means = total_maleODDeaths
    women_means = total_femaleODDeaths

    x = np.arange(len(labels))  
    width = 0.35 

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, men_means, width, label='Moški')
    rects2 = ax.bar(x + width/2, women_means, width, label='Ženske', color = 'pink')

    ax.set_xlabel('Leta')
    ax.set_ylabel('Št. overdosov')
    ax.set_title('Skupno število overdosov')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()


#S klicom spodnjih funkcij laho vidimo, da je v večini več moških, ki predozira, kot pa žensk, razen pri antidepresivih je ravno obratno

# graf_heroin()
# graf_benzodiazepines()
# graf_antidepresivi()
# graf_kokain()
# graf_skupni()