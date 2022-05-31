import bs4
import urllib.request as url
# path = "https://www.flipkart.com/search?q=iphone+12+pro"

product_name = input("Enter thr product name : ")
product_name = product_name.replace(" ", "+")

for n in range(1,6):
    print(f"********Page {n}********")
    path = f"https://www.flipkart.com/search?q={product_name}&page={n}"

    response = url.urlopen(path)
    page = bs4.BeautifulSoup(response)

    titleList = page.find_all('div', {'class' : '_4rR01T'})
    priceList = page.find_all('div', {'class' : '_30jeq3 _1_WHN1'})

    # print(len(titleList), len(priceList))
    for i in range(len(priceList)):
        print("Title :",titleList[i].text)
        print("Price :",priceList[i].text)
        print("*" * 50)
