from __future__ import absolute_import, unicode_literals
from .models import Cyclone_info

from celery import shared_task

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import lxml
import pandas as pd
#scraping function

@shared_task
def cyclone_data():
    print('hello1')
    article_list = []
    try:
        print('Starting the scraping tool')
        r = requests.get('http://rammb-data.cira.colostate.edu/tc_realtime/index.asp')
        soup = BeautifulSoup(r.content, features='html.parser')
        articles = soup.findAll('div', class_='basin_storms')
        print('hello')
        print(articles)
        for a in articles:
            area = a.find('h3').text
            title = a.find('a').text
            image = a.find('a').text
            total = [area,title,image]
            print(total)            
            article = {
                'area': area,
                'title': title,
                'image': image,
                'source': 'cyclone tracking information'
            }
            article_list.append(article)
            print('Finished scraping the articles')
            print(article_list)
            # return save_function(article_list)
        
    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)
    
    
# df = pd.DataFrame({'Title':title}) 
# df.to_csv('products.csv', index=False, encoding='utf-8')
        
@shared_task(serializer='json')
def save_function(article_list):
    print('starting')
    new_count = 0

    for article in article_list:
        try:
            Cyclone_info.objects.create(
                area = article['area'],
                title = article['title'],
                image = article['image'],
                # published = article['published'],
                source = article['source']
            )
            new_count += 1
        except Exception as e:
            print('failed at latest_article is none')
            print(e)
            break
    return print('finished')

cyclone_data()
