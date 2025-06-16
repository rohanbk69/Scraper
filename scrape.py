import json
import requests
from bs4 import BeautifulSoup


url="http://books.toscrape.com/"


def scrape_book(url):
    response=requests.get(url)
    
    # Set encoding explicitly to handle special cahracter correctly
    response.encoding=response.apparent_encoding
    # print(response.status_code)
    
    if response.status_code!=200:
        return
    
    soup=BeautifulSoup(response.text,"html.parser")
    books=soup.find_all("article",class_="product_pod")
    
    data=[]
    
    for book in books:
    
        title=book.h3.a["title"]
    
        price_text=book.find("p",class_="price_color").text
        
        currency=price_text[0]
        price=float(price_text[1:])
        
        # print(title,currency,price)
        
        data.append({
            "name":title,
            "currency":currency,
            "price":price,
            
        }) 
        
    with open("data.json","w",encoding="utf-8") as file:
        json.dump(data,file,indent=2,ensure_ascii=False)
        

       
    
        
                
scrape_book(url)


# go to git bash
# git config --global user.name "Rohan Bk"
# git config --global user.email "rohan7study@gmail.com"

# git init -> initalize git
# git status -> if u want to check what are the status of the file
# git diff -> if u want to check what are the changes
# git add .
# git commit -m "Your message"
#copy paste git code from github


#Change the code
# 1. git add .
# 2. git commit -m "Your Message"
# 3. git push