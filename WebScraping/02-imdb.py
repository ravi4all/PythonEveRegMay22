import bs4
import urllib.request as url

path = "https://www.imdb.com/title/tt4154796/?ref_=nv_sr_srsg_1"
response = url.urlopen(path)
page = bs4.BeautifulSoup(response)

title = page.find('h1', {'class' : 'sc-b73cd867-0'})
print("Title :",title.text)

rating = page.find('span', {'class' : 'sc-7ab21ed2-1'})
print("Rating :",rating.text)

summary = page.find('span', {'class' : 'sc-16ede01-2'})
print("Summary :",summary.text)