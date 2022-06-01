Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import json
import urllib.request as url
response = url.urlopen("https://data.covid19india.org/states_daily.json")
data = json.load(response)
type(data)
<class 'dict'>
data.keys()
dict_keys(['states_daily'])
states = data["states_daily"]
type(states)
<class 'list'>
len(states)
1563
states[0]
{'an': '0', 'ap': '1', 'ar': '0', 'as': '0', 'br': '0', 'ch': '0', 'ct': '0', 'date': '14-Mar-20', 'dateymd': '2020-03-14', 'dd': '0', 'dl': '7', 'dn': '0', 'ga': '0', 'gj': '0', 'hp': '0', 'hr': '14', 'jh': '0', 'jk': '2', 'ka': '6', 'kl': '19', 'la': '0', 'ld': '0', 'mh': '14', 'ml': '0', 'mn': '0', 'mp': '0', 'mz': '0', 'nl': '0', 'or': '0', 'pb': '1', 'py': '0', 'rj': '3', 'sk': '0', 'status': 'Confirmed', 'tg': '1', 'tn': '1', 'tr': '0', 'tt': '81', 'un': '0', 'up': '12', 'ut': '0', 'wb': '0'}
states[1]
{'an': '0', 'ap': '0', 'ar': '0', 'as': '0', 'br': '0', 'ch': '0', 'ct': '0', 'date': '14-Mar-20', 'dateymd': '2020-03-14', 'dd': '0', 'dl': '1', 'dn': '0', 'ga': '0', 'gj': '0', 'hp': '0', 'hr': '0', 'jh': '0', 'jk': '0', 'ka': '0', 'kl': '3', 'la': '0', 'ld': '0', 'mh': '0', 'ml': '0', 'mn': '0', 'mp': '0', 'mz': '0', 'nl': '0', 'or': '0', 'pb': '0', 'py': '0', 'rj': '1', 'sk': '0', 'status': 'Recovered', 'tg': '0', 'tn': '0', 'tr': '0', 'tt': '9', 'un': '0', 'up': '4', 'ut': '0', 'wb': '0'}
states[0]['dl']
'7'
states[200]['dl']
'6'
states[400]['dl']
'2137'
states[400]['status']
'Recovered'
states[399]['dl']
'1142'
states[399]['date']
'25-Jul-20'
