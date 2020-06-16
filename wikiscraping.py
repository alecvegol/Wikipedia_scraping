import requests


#Getting the HTML of the website:
url= 'https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area'
# requesting HTML of the website:
response = requests.get(url).text

from bs4 import BeautifulSoup
soup = BeautifulSoup(response,'lxml')
#print(soup.prettify()) #to check the connection

#extracting the whole table first:
My_table = soup.find('table',{'class':'wikitable sortable'})

#print(My_table) #checking the result

#extracting the rows with county name in it
countries = My_table.find_all('a')
#print(countries)

#going through the lines with names of countries and extract the names of the countries
European_counteries=[]
count=1
for i in countries:
    European_counteries.append(i.get('title'))
    count=count+1
print(European_counteries)
    
#creating dataframe for the data    
import pandas as pd
df = pd.DataFrame(European_counteries)
#df['Country'] = European_counteris

print(df)
