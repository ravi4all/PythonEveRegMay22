import bs4
import urllib.request as url
path = "https://www.flipkart.com/search?q=iphone+12"

response = url.urlopen(path)
page = bs4.BeautifulSoup(response)
page.find('div', {'class' : '_4rR01T'})

title = page.find('div', {'class' : '_4rR01T'})
print("Title :",title.text)

price = page.find('div', {'class' : '_30jeq3 _1_WHN1'})
print("Price :",price.text)