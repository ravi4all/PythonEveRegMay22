import urllib.request as url
import json

path = "https://api.covid19india.org/states_daily.json"
response = url.urlopen(path)
data = json.load(response)
states = data["states_daily"]
print(states[0])

confirmed_data = []
recovered_data = []
deceased_data = []

for i in range(len(states)):
    if states[i]['status'] == 'Confirmed':
        confirmed_data.append(states[i])
    elif states[i]['status'] == 'Recovered':
        recovered_data.append(states[i])
    else:
        deceased_data.append(states[i])

dl_conf_cases = 0
dl_dec_cases = 0
dl_rec_cases = 0
for i in range(len(confirmed_data)):
    dl_conf_cases += int(confirmed_data[i]['dl'])
    dl_rec_cases += int(recovered_data[i]['dl'])
    dl_dec_cases += int(deceased_data[i]['dl'])

print("Total Confirmed Cases in Delhi :",dl_conf_cases)
print("Total Recovered Cases in Delhi :",dl_rec_cases)
print("Total Deceased Cases in Delhi :",dl_dec_cases)
