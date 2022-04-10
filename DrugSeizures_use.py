import requests
import simplejson as json
import numpy as np
import matplotlib.pyplot as plt
url = "http://127.0.0.1:5000/DrugSeizuresPost"

payload = json.dumps({
  "Year": 2019,
  "Region": False,
  "Country": "Slovenia",
  "DrugGroup": False,
  "Drug": False,
  "Code": False
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
jsondata = response.json()
jsondata = jsondata["data"]
drugs = []
kg = []
print(jsondata)
for el in jsondata:
  drugs.append(el["Drug"])
  kg.append(el["Kilograms"])


print(kg)
print(drugs)
y_pos = np.arange(len(drugs))

fig, ax = plt.subplots()
ax.barh(y_pos, kg, align='center')
ax.set_yticks(y_pos)
ax.invert_yaxis()
ax.set_xlabel('Kg')
plt.show()
