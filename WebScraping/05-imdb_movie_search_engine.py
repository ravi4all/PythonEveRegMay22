import urllib.request as url
import bs4

userInput = input("Enter movie name : ")
userInput = userInput.replace(" ", "+").lower()
path = f"https://www.imdb.com/find?q={userInput}&ref_=nv_sr_sm"

response = url.urlopen(path)
page = bs4.BeautifulSoup(response, 'lxml')

td = page.find('td', {'class' : 'result_text'})
a_tag = td.find('a')
href = a_tag['href']

path = "https://www.imdb.com" + href

response = url.urlopen(path)
page = bs4.BeautifulSoup(response, "lxml")

title = page.find('h1', {'class' : 'sc-b73cd867-0'})
print("Title :",title.text)

rating = page.find('span', {'class' : 'sc-7ab21ed2-1'})
print("Rating :",rating.text)

summary = page.find('span', {'class' : 'sc-16ede01-2'})
print("Summary :",summary.text)