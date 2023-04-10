from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import requests
from bs4 import BeautifulSoup

# Create your views here.

url="https://www.flipkart.com/search?q=oppo+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=oppo+mobiles%7CMobiles&requestId=ee949858-bcc9-4975-9230-493a2f584c61"
response=requests.get(url)
soup=BeautifulSoup(response.content,"html.parser")
title = soup.find_all("div",class_="_4rR01T")
oppo_titles=[]
for i in title:
    title = i.get_text()
    oppo_titles.append(title)

images = soup.find_all("img",class_="_396cs4")
oppo_images=[]
for j in images:
    image = j['src']
    oppo_images.append(image)

links = soup.find_all("a",class_="_1fQZEK")
oppo_links=[]
for k in links:
    link = "https://www.flipkart.com"+k['href']
    oppo_links.append(link)

price = soup.find_all("div",class_="_30jeq3 _1_WHN1")
oppo_price=[]
for l in price:
    prices = l.get_text()
    oppo_price.append(prices)
    
oppo_list=zip(oppo_links, oppo_price, oppo_titles, oppo_images)

@login_required(login_url='login')
def oppo(request):
    if request.user.is_authenticated:
        return render(request,"oppo.html",{"oppo_list":oppo_list})
    return redirect("login")
