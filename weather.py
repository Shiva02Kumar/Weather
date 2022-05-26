import requests
from bs4 import BeautifulSoup

url = 'https://www.timeanddate.com/weather/'

country = input("Enter Country : ")
state = input("Enter State/City : ")

country = country.strip()
state = state.strip()
url = url + country.lower() + "/" + state.lower()

r = requests.get(url)

if not r:
    print("Country or State not found")
    exit(0)

htmlcontent = r.content
soup = BeautifulSoup(htmlcontent,'html.parser')

weather1 = soup.find(id = 'qlook')
weather = weather1.find_all("div", class_="h2")
predict = weather1.p
predict1 = predict.find_next_sibling("p")
pre = predict1.contents

pre1 = []
for i in pre:
    if (i.string != None):
        pre1.append(i.string)

for temp in weather:
    print("Todays Temprature is = " + temp.string)

print(predict.string ,end=' ')

for extra in pre1:
    print(extra + ',', end=' ')
