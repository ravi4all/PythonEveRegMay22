import bs4
import urllib.request as url

for i in range(1,53,51):
    path = f"https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&start={i}&ref_=adv_nxt"

    response = url.urlopen(path)
    # lxml - library xml
    page = bs4.BeautifulSoup(response, "lxml")

    # title = page.find('h3', {'class' : 'lister-item-header'})
    # rating = page.find('div', {'class' : 'ratings-imdb-rating'})

    # print(title.text.strip().replace("\n"," "))
    # print(rating.text.strip())

    titleList = page.find_all('h3', {'class' : 'lister-item-header'})
    ratingList = page.find_all('div', {'class' : 'ratings-imdb-rating'})

    for j in range(len(titleList)):
        print(titleList[j].text.strip().replace("\n"," "))
        print(ratingList[j].text.strip())
        print("*" * 30)

