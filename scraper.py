#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
print("imported")


# In[2]:


import requests


# In[ ]:





# In[27]:


url="https://magicpin.in/blog/best-restaurants-chennai/#:~:text=A%20Foodie%20Guide%20To%20A%20Paradise%20Of%20The,...%208%208.%20Kailash%20Kitchen%20...%20More%20items"
data=requests.get(url)
if data.status_code==200:
    print("success")
else:
    print("failed")


# In[83]:


soup=BeautifulSoup(data.text,"html.parser")


# In[101]:


content=soup.find_all('div',class_="blog-content")
restaurant_names=[]
for con in content:
    tag=con.find_all('h3')
    for h3tag in tag:
        restaurant_names.append(h3tag.text.strip())
restaurant_names=restaurant_names[:15]  
del restaurant_names[2]
print(restaurant_names)
    


# In[102]:


loc=[]
location_tags=con.find_all('p')
for p in location_tags:
    if 'Location:' in p.text:
        loc_split=p.text.split(':')
        if len(loc_split)>1:
            location = loc_split[1].strip()
            loc.append(location)
            
print(loc)    


# In[114]:


import pandas as pd
dict_l={'Restaurants':restaurant_names,
     'Locations':loc}
df1=pd.DataFrame(dict_l)
df1.head(14)        


# In[117]:


df1['Restaurants']=df['Restaurants'].apply(lambda x: x.split('.',1)[1].strip() if x[1] == '.' else x)
df1


# In[127]:


df1["Locations"]=df1['Locations'].apply(lambda x: x[:-16] if x.endswith("(Get Directions)")else x)
df1


# In[129]:


df1.to_csv('C:/Users/manov/Downloads/restaurants.csv',index=False)


# In[ ]:




