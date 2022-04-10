import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import simplejson as json
# Aretacije zaradi drog med leti [1980,2015] v Ameriki

#Pridobivanje podatkov
podatki = pd.read_excel('Arrests.xlsx')
df = pd.DataFrame(podatki)

leta = df.iloc[0][1:]
drug_abuse_violations = df.iloc[8][1:]
sales_and_manufacturing = df.iloc[9][1:]
possesions = df.iloc[10][1:]


sl = {'Leta': [],
    'Zlorabe': [],
    'Prodaja in proizvodnja': [],
    'Posesti': []}

for leto in leta:
    sl['Leta'] += [int(leto)]

for zloraba  in drug_abuse_violations:
    sl["Zlorabe"] += [int(zloraba)]

for prodaja in sales_and_manufacturing:
    sl["Prodaja in proizvodnja"] += [int(prodaja)]

for posest in possesions:
    sl['Posesti'] += [posest]

print(sl)
with open("OverDose.json", "w") as outfile:
    json.dump(sl, outfile, ignore_nan=True)
#Primerjava stevila aretacij zaradi določenega zločina

st_aretacij_zaradi_posesti = 0
for st in sl['Posesti']:
    st_aretacij_zaradi_posesti += int(st)
#print(st_aretacij_zaradi_posesti)

st_aretacij_zaradi_zlorabe = 0
for st in sl['Zlorabe']:
    st_aretacij_zaradi_zlorabe += int(st)
#print(st_aretacij_zaradi_zlorabe)

st_aretacij_zaradi_prodaje = 0
for st in sl['Prodaja in proizvodnja']:
    st_aretacij_zaradi_prodaje += int(st)
#print(st_aretacij_zaradi_prodaje)

skupno_aretacij = { 
    'Prodaja in Proizvodnja': st_aretacij_zaradi_prodaje,
    'Zloraba': st_aretacij_zaradi_zlorabe,
    'Posesti': st_aretacij_zaradi_posesti
}

najvec_aretacij = []
for st in skupno_aretacij.values():
    najvec_aretacij.append(st)
    najvec_aretacij = sorted(najvec_aretacij)
for kljuc in skupno_aretacij.keys():
    if skupno_aretacij[kljuc] == max(najvec_aretacij):
        print((kljuc,max(najvec_aretacij)))                 # Vidimo da je bilo največ aretacij zaradi zlorabe drog
    elif skupno_aretacij[kljuc] == min(najvec_aretacij):    # Najmanj je bilo posesti droge
        print((kljuc,min(najvec_aretacij)))
    else:
        print((kljuc,najvec_aretacij[1]))   	            # Zlorabe drog je bilo drugo največ



years = map(str,sl['Leta'])
print(years)


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Prodaja in proizvodnja', 'Zloraba', 'Posesti'
sizes = [10473302,47924215,37450908]
explode = (0, 0.1, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')

plt.show()