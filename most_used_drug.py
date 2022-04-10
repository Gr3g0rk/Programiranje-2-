from collections import Counter
import pygal
from pygal.style import Style
  
# Slovar z najbolj uporabljenimi drogami leta 2020 za večino držav (Vir: https://www.visualcapitalist.com/mapped-the-most-common-illicit-drugs-in-the-world/)
najbolj_uporabljenje_droge = {
    'af': 'Heroin',
    'al': 'Pomirjevala',
    'dz': 'Konoplja',
    'ar': 'Konoplja',
    'au': 'Konoplja',
    'az': 'Heroin',
    'bh': 'Konoplja',
    'bd': 'Amfetamin',
    'by': 'Opij',
    'be': 'Konoplja',
    'bo': 'Konoplja',
    'bn': 'Konoplja',
    'bg': 'Konoplja',
    'bf': 'Konoplja',
    'ca': 'Konoplja',
    'cf': 'Konoplja',
    'cl': 'Konoplja',
    'ch': 'Metamfetamin',
    'cr': 'Konoplja',
    'ci': 'Konoplja',
    'hr': 'Heroin',
    'cy': 'Konoplja',
    'cz': 'Benzodiazepini',
    'do': 'Kokain',
    'ec': 'Konoplja',
    'sv': 'Konoplja',
    'ee': 'Konoplja',
    'fi': 'Konoplja',
    'fr': 'Konoplja',
    'ge': 'Konoplja',
    'de': 'Konoplja',
    'gr': 'Inhalanti',
    'gt': 'Konoplja',
    'hn': 'Konoplja',
    'hk': 'Heroin',
    'hu': 'Konoplja',
    'is': 'Konoplja',
    'in': 'Heroin',
    'id': 'Konoplja',
    'ir': 'Opij',
    'ie': 'Konoplja',
    'il': 'Konoplja',
    'it': 'Konoplja',
    'jp': 'Metamfetamin',
    'jo': 'Konoplja',
    'ke': 'Konoplja',
    'lv': 'Konoplja',
    'ly': 'Konoplja',
    'li': 'Konoplja',
    'lt': 'Pomirjevala',
    'lu': 'Konoplja',
    'mo': 'Metamfetamin',
    'mg': 'Konoplja',
    'my': 'Metamfetamin',
    'mt': 'Heroin',
    'mx': 'Konoplja',
    'md': 'Konoplja',
    'mn': 'Metamfetamin',
    'mz': 'Konoplja',
    'mm': 'Heroin',
    'nl': 'Benzodiazepini',
    'nz': 'Metamfetamin',
    'ni': 'Konoplja',
    'ng': 'Konoplja',
    'no': 'Konoplja',
    'om': 'Opij',
    'pk': 'Konoplja',
    'pa': 'Konoplja',
    'pe': 'Opij',
    'ph': 'Konoplja',
    'pl': 'Konoplja',
    'pt': 'Konoplja',
    'ro': 'Konoplja',
    'sn': 'Konoplja',
    'rs': 'Benzodiazepini',
    'sg': 'Metamfetamin',
    'si': 'Konoplja',
    'za': 'Konoplja',
    'kp': 'Metamfetamin',
    'es': 'Konoplja',
    'lk': 'Konoplja',
    'sd': 'Konoplja',
    'sr': 'Konoplja',
    'se': 'Konoplja',
    'sz': 'Konoplja',
    'sy': 'Konoplja',
    'tj': 'Heroin',
    'tz': 'Konoplja',
    'th': 'Metamfetamin',
    'tg': 'Konoplja',
    'tn': 'Konoplja',
    'tr': 'Konoplja',
    'tm': 'Opij',
    'us': 'Konoplja',
    'gb': 'Konoplja',
    'ua': 'Opij',
    'uy': 'Konoplja',
    'uz': 'Konoplja',
    've': 'Benzodiazepini',
    'vn': 'Heroin',
    'zm': 'Konoplja',
}


stevilo_porab = Counter(najbolj_uporabljenje_droge.values())
print(stevilo_porab)                                            # Najpopularnejša droga je konoplja, nato sta heroin in opij, nato so benzodiazepini,
                                                                # za njimi sledijo pomirjevala, zadnje mesto si pa delijo amfetamini, kokain in inhalanti

# S pomočjo spodnje kode bova prikazala zemljevid sveta, kjer bo vsaka država obarvana v svojo barvo, ki bo ustrezala najpopularnejši drogi v državi
konoplja = []
metamfetamin = []
heroin = []
opij = []
benzodiazepini = []
pomirjevala = []
kokain = []
amfetamin = []
inhalanti = []

for kljuc in najbolj_uporabljenje_droge.keys():
    if najbolj_uporabljenje_droge[kljuc] == 'Konoplja':
        konoplja.append(kljuc)
    elif najbolj_uporabljenje_droge[kljuc] == 'Metamfetamin':
        metamfetamin.append(kljuc)
    elif najbolj_uporabljenje_droge[kljuc] == 'Heroin':
        heroin.append(kljuc)
    elif najbolj_uporabljenje_droge[kljuc] == 'Opij':
        opij.append(kljuc)
    elif najbolj_uporabljenje_droge[kljuc] == 'Benzodiazepini':
        benzodiazepini.append(kljuc)
    elif najbolj_uporabljenje_droge[kljuc] == 'Pomirjevala':
        pomirjevala.append(kljuc)
    elif najbolj_uporabljenje_droge[kljuc] == 'Kokain':
        kokain.append(kljuc)
    elif najbolj_uporabljenje_droge[kljuc] == 'Amfetamin':
        amfetamin.append(kljuc)
    elif najbolj_uporabljenje_droge[kljuc] == 'Inhalanti':
        inhalanti.append(kljuc)



custom_style = Style( colors = ('#FF0000' , '#0000FF' ,
                                '#00FF00' , '#000000',
                                '#FFD700'))
  
worldmap =  pygal.maps.world.World(style = custom_style)
  
worldmap.title = 'Uporaba drog po državah'
  
worldmap.add('Konoplja', konoplja)
  
worldmap.add('Kokain', kokain)
  
worldmap.add('Amfetamin', amfetamin)
  
worldmap.add('Inhalanti',inhalanti)
  
worldmap.add ('Benzodiazepini', benzodiazepini)

worldmap.add('Heroin', heroin)

worldmap.add('Pomirjevala', pomirjevala)

worldmap.add('Opij', opij)

worldmap.add('Metanfetamin', metamfetamin)
  

# Za bolši prikaz najuporabnejših drog po svetu moramo odpreti datoteko 'svet.svg', ki nam bo v brskalniku prikazala zemljevid sveta in najbolj uporabljene
# droge v posamezni državi
worldmap.render_to_file('svet.svg')

  
