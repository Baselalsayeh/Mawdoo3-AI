#!/usr/bin/env python
# coding: utf-8

# In[12]:


import requests

def segmentation():
    txt=input("Please enter the text you want to segment.")
    url='https://api.mawdu.com/text/AIv3/segment?text='
    r1 = requests.get(url+txt, headers={'x-api-key':'dkbqeOghAKaWsGUFpW2CD4LvL0RvHNbj54x348kR'}).json()
    print(r1)
    
def topic():
    txt=input("Please enter the text you want to find its topic.")
    url='https://api.mawdu.com/text/AIv3/topics?limit=&text='
    r1 = requests.get(url+txt, headers={'x-api-key':'dkbqeOghAKaWsGUFpW2CD4LvL0RvHNbj54x348kR'}).json()
    print(r1)
    
def sentiment():
    txt=input("Please enter the text you want to find its sentiment.")
    url='https://api.mawdu.com/text/AIv3/sentiment?text='
    r1 = requests.get(url+txt, headers={'x-api-key':'dkbqeOghAKaWsGUFpW2CD4LvL0RvHNbj54x348kR'}).json()
    print(r1)
    
def similar():
    txt=input("Please enter the word you want to find its similarities.")
    url='https://api.mawdu.com/text/AIv3/similar?word='
    r1 = requests.get(url+txt, headers={'x-api-key':'dkbqeOghAKaWsGUFpW2CD4LvL0RvHNbj54x348kR'}).json()
    print(r1)
    
    
def tashkeel():
    txt=input("Please enter the text you want to tashkeel.")
    url='https://api.mawdu.com/text/AIv3/tashkeel?silence=&sentence='
    r1 = requests.get(url+txt, headers={'x-api-key':'dkbqeOghAKaWsGUFpW2CD4LvL0RvHNbj54x348kR'}).json()
    print(r1)
    

    

op=int(input("welcome to Mawdoo3 text APIs \n please select the operation: \n 1.segmentation \n 2.topic \n 3.sentiment \n 4.similar \n 5.tashkeel \n"))

if op==1:
    segmentation()
elif op==2:
    topic()
elif op==3:
    sentiment()
elif op==4:
    similar()
elif op==5:
    tashkeel()
else:
    print("choise not available, please select a valid choise!!!")















