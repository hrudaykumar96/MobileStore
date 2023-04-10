from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import requests
from bs4 import BeautifulSoup

# Create your views here.

url = "https://www.flipkart.com/search?q=mi+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mi+mobiles%7CMobiles&requestId=ee949858-bcc9-4975-9230-493a2f584c61"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
title = soup.find_all("div", class_="_4rR01T")
mi_titles = []
for i in title:
    title = i.get_text()
    mi_titles.append(title)

images = soup.find_all("img", class_="_396cs4")
mi_images = []
for j in images:
    image = j['src']
    mi_images.append(image)

links = soup.find_all("a", class_="_1fQZEK")
mi_links = []
for k in links:
    link = "https://www.flipkart.com"+k['href']
    mi_links.append(link)

price = soup.find_all("div", class_="_30jeq3 _1_WHN1")
mi_price = []
for l in price:
    prices = l.get_text()
    mi_price.append(prices)

mi_list = zip(mi_links, mi_price, mi_titles, mi_images)


@login_required(login_url='login')
def mi(request):
    if request.user.is_authenticated:
        return render(request, "mi.html", {"mi_list": mi_list})
    return redirect("login")