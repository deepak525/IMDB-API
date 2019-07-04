#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
from tqdm import tnrange


# In[3]:


movie_name = []
cast = []
ids = []
genre = []
runtime = []
ratings = []


def split_cast(lists):
    a = lists[2].text
    idx = a.find('Stars:')
    sp = ("".join(a[idx+6:].split('\n'))).strip()
    sp = sp.split(',')
    my_list = []
    for i in range(len(sp)):
        my_list.append(sp[i].strip())
    return my_list

for i in tnrange(1,11):
    html = requests.get("https://www.imdb.com/list/ls006266261/?sort=user_rating,desc&st_dt=&mode=detail&page="+str(i))
    soup = BeautifulSoup(html.content, "html5lib")
    for movie in soup.select('div.lister-item-content'):
        movie_name.append((movie.find("a")).text)

        ids.append(((movie.find("a"))['href']).split('/')[2])

        genre.append(((movie.find('span','genre')).text).split())

        runtime.append(int(((movie.find('span','runtime')).text).split()[0]))

        ratings.append(float(((movie.find('span','ipl-rating-star__rating')).text).split()[0]))

#         temp = movie.findAll('p',{'class':"text-muted text-small"})
#         temp_cast = []
#         for tag in temp[1].findAll('a'):
#             temp_cast.append(tag.text)
#         cast.append(temp_cast)

        cast.append(split_cast((movie.findAll("p"))))


# In[4]:


final_data = []
for i in range(len(movie_name)):
    dicts = {}
    dicts['id'] = ids[i]
    dicts['movie_name'] = movie_name[i]
    dicts['cast'] = cast[i]
    dicts['rating']=  ratings[i]
    dicts['runtime'] = runtime[i]
    dicts['genre'] = genre[i]
    final_data.append(dicts)


# In[5]:


from pymongo import MongoClient
client = MongoClient()

client = MongoClient('mongodb://localhost:27017/')
db = client['IMDB']
collection = db['movies_data']


# In[6]:


for i in final_data:
    db.movies_data.insert_one(i)


# In[ ]:


curr = collection.find()
for i in curr:
    print(i)

