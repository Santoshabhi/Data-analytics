!pip install bs4
from bs4 import BeautifulSoup
import requests as req
import pandas as pd
r=req.get("https://visaguide.world/asia/#google_vignette")
s=BeautifulSoup(r.text,"html.parser")
ta=s.find_all("table")
table=ta[1]


cols=ta[1].find_all("th")
columes=[]
for i in cols:
    columes.append(i.text)


rows=ta[1].find_all("td")
country=[]
for i in rows[::4]:
    country.append(i.text.strip())

capital=[]
for i in rows[1::4]:
    capital.append(i.text.strip())

area=[]
for i in rows[2::4]:
    area.append(i.text.strip())

population=[]
for i in rows[3::4]:
    population.append(i.text.strip())
dic={}
dic.update({columes[0]:country})
dic.update({columes[1]:capital})
dic.update({columes[2]:area})
dic.update({columes[3]:population})

data=pd.DataFrame(dic)
data.to_csv("listofcountriesinasia.csv")
data
