from bs4 import BeautifulSoup
from datetime import datetime
import requests



writer          =       open('TopSteam.txt','a')
tim             =       datetime.now().strftime("%d/%m/%Y %H:%M:%S")       
print(tim)

link            =       requests.get('https://store.steampowered.com/search/?sort_by=Released_DESC&term=rpg').text

soup            =       BeautifulSoup(link,'lxml')

containers      =       soup.find_all('div',class_='responsive_search_name_combined')

writer.write(tim)
writer.write("\n")

for container in containers:
    name            =   container.find('span',class_='title')
    date            =   container.find('div',class_='col search_released responsive_secondrow')

    
    
    #All games have dicounted and price tag   
    
    discount_prices =   container.find('div',class_='col search_price discounted responsive_secondrow')
    prices          =   container.find('div',class_='col search_price responsive_secondrow')       
    
    if(discount_prices!=None):    
        price=discount_prices.find('span').text.strip()          # In case there is a dicount don't Store OG price find and store ptice after disount only
    
    elif((discount_prices==None) and prices!=None):
        price=prices.text.strip()                                # Store regular price if no disount
        
        if(price==''):
            price='Price cannot be found'
    
    
    
    writ=(f'''
Name                :   {name.text}

Date Released       :   {date.text}    

Price               :   {price}    
    
    ''')


    print(writ)
    writer.write(writ)
writer.close()