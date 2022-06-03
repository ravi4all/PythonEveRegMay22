import urllib.request as url
import json

q = "mr bean"
q = q.replace(" ", "+")
api_key = "1gPMgQWU9fDU9PPHW2Kr917sPJlo3n2g"
limit = 10
path = f"http://api.giphy.com/v1/gifs/search?q={q}&api_key={api_key}&limit={limit}"

response = url.urlopen(path)
data = json.load(response)
data = data['data']
for i in range(len(data)):
    images = data[i]['images']
    img_url = images['original']['url']
    url.urlretrieve(img_url, f'images/img_{i}.gif')