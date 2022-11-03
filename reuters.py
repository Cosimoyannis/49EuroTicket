url_others = 'ftp://ftp.nasdaqtrader.com/symboldirectory/otherlisted.txt'

import pandas
df1 = pandas.read_csv(url_others, sep = '|')

stocks = df1['ACT Symbol'].tolist()

import requests
from bs4 import BeautifulSoup

news_list = list()
for x in stocks[0:15]:
    
    url = 'https://www.reuters.com/markets/companies/' + x + '.N/profile'
	#Google Chrome - Menu - Weitere Tools - Entwicklertools
	#Ctrl+Shift+C - Select section of interest
	#Right click html code and copy XPath:
    page = requests.get(url).content
    print(url)

    soup = BeautifulSoup(page, 'lxml')

    try:
        for i in range(1):
            news = soup.body.find(id="main-content").find_all("li", {"class": lambda c: c and 'story-collection' in c})
            for n in news:
                message = n.find('a', {"data-testid" : "Heading"}).get_text()
                time = str.split(n.find('time').get_text())
                news_list.append([x,time[0],time[1],'2022',message])
    except:
        message == message
  
        print('No findings.')

news_df = pandas.DataFrame(news_list, columns=['StockID','Month','Day','Year','News'])
news_df.to_csv("reuters.csv")