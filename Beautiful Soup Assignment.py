#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1) Write a python program to display IMDB’s Top rated 100 Indian movies’ data 
# https://www.imdb.com/list/ls056092300/ (i.e. name, rating, year of release) and make data frame. 

get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[12]:


page= requests.get('https://www.imdb.com/list/ls056092300/')
page


# In[13]:


soup= BeautifulSoup(page.content)
soup


# In[ ]:


# We can not get data since response range is more than 299


# In[ ]:





# In[16]:


# 2)Write a python program to scrape details of all the posts from https://www.patreon.com/coreyms 
#Scrap the heading, date, content and the likes for the video from the link for the youtube video from the post. 

page = requests.get('https://www.patreon.com/coreyms')
page


# In[36]:


soup1= BeautifulSoup(page.content)
soup1


# In[47]:


heading=[]
for i in soup1.find_all('div', class_="sc-bBHxTw iloeMK"):
    heading.append(i.text)

heading


# In[38]:


date= []
for i in soup1.find_all('div', class_="sc-lgu5zg-0 gDgFXW"):
    date.append(i.text)
    
date


# In[46]:


content= []
for i in soup1.find_all('div', class_="sc-jrQzAO jogWkF"):
    content.append(i.text)
    
content


# In[ ]:





# In[40]:


# Question 3.Write a python program to scrape house details from mentioned URL. 
#It should include house title, location, area, EMI and price from https://www.nobroker.in/ .
#Enter three localities which are Indira Nagar, Jayanagar, Rajaji Nagar.  


page= requests.get('https://www.nobroker.in/')
page


# In[42]:


soup2= BeautifulSoup(page.content)
soup2


# In[50]:


title= []
for i in soup2.find_all('div', class_="nb__1YnwY"):
    title.append(i.text)
    
title


# In[53]:


Location= []
for i in soup2.find_all('div', class_="css-1hwfws3 nb-select__value-container nb-select__value-container--has-value"):
    Location.append(i.text)
    
Location


# In[ ]:


EMI= []
for i in soup2.finad_all('div', )


# In[ ]:





# In[54]:


# 4)	Write a python program to scrape first 10 product details which include product name , price , Image 
# URL from https://www.bewakoof.com/bestseller?sort=popular . 


page= requests.get('https://www.bewakoof.com/bestseller?sort=popular')
page


# In[58]:


soup3= BeautifulSoup(page.content)
soup3


# In[64]:


name= []
for i in soup3.find_all('div', class_="productNaming bkf-ellipsis"):
    name.append(i.text)
    
name


# In[90]:


price= []
for i in soup3.find_all('div', class_="discountedPriceText clr-p-black   false"):
    price.append(float(i.text))

price


# In[89]:


image = []
for i in soup3.find_all('div', class_="productImg"):
    image.append(i.['data-src'])

image


# In[ ]:





# In[91]:


# 5)	Please visit https://www.cnbc.com/world/?region=world and scrap-     a)   headings 
# b)	date 
# c)	News link 


page= requests.get('https://www.cnbc.com/world/?region=world')
page


# In[92]:


soup4= BeautifulSoup(page.content)
soup4


# In[93]:


heading= []
for i in soup4.find_all('div', class_="FeaturedCard-contentText"):
    heading.append(i.text)
    
heading


# In[ ]:


date= []
for i in soup4.find_all()


# In[95]:


link= []
for i in soup4.find_all('li', class_="CNBCFooter-listItem"):
    link.append(i.text)
    
link


# In[ ]:





# In[96]:


#6)	Please visit  https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloadedarticles/  
# and scrap-  a)	Paper title b)	date c)	Author 


page= requests.get('https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloadedarticles/')
page


# In[97]:


soup5 = BeautifulSoup(page.content)
soup5


# In[100]:


title = []
for i in soup5.find_all('li', class_="mb-1"):
    title.append(i.text)
    
title


# In[ ]:


date = []
for i in soup5.find_all('li', class_="mb-1"):


# In[ ]:





# In[ ]:




