# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 16:45:45 2017

@author: Venkata Praveen Dusi
"""


import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import re
import time
import numpy as np
from collections import OrderedDict
import json



ARTTITLE_S = []
SECTION_INFO_S = []
AUTHORS = []
ABSTRACTS=[]
KEYWORDS=[]
D=OrderedDict()

'''Looping with urls:'''
url = 'http://pubsonline.informs.org/toc/isre/'
v = 1
while v<29:
    url_n = url +str(v)+'/'
    count = 1
    while count<5:
        url_n1 = url_n + str(count)
        print('now scrapping data from : ', url_n1)
        
        driver = webdriver.Chrome("C:/Users/Venkata Praveen Dusi/Documents/chromedriver.exe")
        driver.get(url_n1)
        
        try:      
        
            checkboxes = driver.find_elements_by_xpath("//input[@name='doi']")
            for checkbox in checkboxes:
                if not checkbox.is_selected():
                    checkbox.click()
            driver.find_element_by_partial_link_text('View Abstracts').click()
            
            current_url=driver.current_url
            
            page = requests.get(current_url)
            soup = BeautifulSoup(page.content, 'html.parser')
                        
            '''#Section Info'''
            section_info = []
            section_info_s = []
            section_info = driver.find_elements_by_class_name('sectionInfo')
            for s in section_info:
                 section_info_s.append(s.text)
            del section_info_s[1::2]
            
            SECTION_INFO_S.append(section_info_s)
            print('appended section info list')
            
            ''' #Article Titles''' 
            arttitle = []
            arttitle_s = []
            arttitle = driver.find_elements_by_class_name('arttitle')
            for title in arttitle:
                arttitle_s.append(title.text)
            
            ARTTITLE_S.append(arttitle_s)
            print('appended article title list')
            
            ''' #Authors'''
            lst = []
            a_tags = soup.h1.find_all_next('span')
            for a in a_tags:
                lst.append(a.text)
            
            from itertools import groupby
                        
            aut=[list(group) for k, group in groupby(lst, lambda x: ((x == 'Keywords') or (x=='Key Words'))) if not k]
            len(aut)
            
                                  
            for l in aut:
                del l[1::2]
            
            AUTHORS.append(aut)
            print('appended authors list')    
            
            '''#Abstract'''
            abstract = []
            abstract_s = []
            abstract = driver.find_elements_by_class_name('abstractSection')
            for a in abstract:
                 abstract_s.append(a.text)
            
            ABSTRACTS.append(abstract_s)
            print('appended abstracts list')
            
            '''#KeyWords'''
            
            keywords=[]
            a_tags = soup.find_all("div",class_="abstractKeywords")
            for a in a_tags:
                keywords.append(a.text)
        
            
            '''# Create a function called "chunks" with two arguments, l and n:'''
            def chunks(l, n):
                # For item i in a range that is a length of l,
                for i in range(0, len(l), n):
                    # Create an index range for l of n items:
                    yield l[i:i+n]
            
            keywords1=list(chunks(keywords,1))
            
            for i in range(0,len(keywords1)):
                new=keywords1[i][0].split(';')[:]
                try:
                    new[0] = new[0].split(':')[1]
                except IndexError:
                    pass
                keywords1[i] = new
            KEYWORDS.append(keywords1)
            print('appended keywords list')
            
            num_articles = len(keywords1)
            print('number of articles : ',num_articles )
            
            '''Create dictionary and push all the values  '''
            key = ['year','volume','issue','title','authors','keywords','abstract']
    
            p=[]
            for i in range(0,len(keywords1)):
                d =OrderedDict()
                try:
                    d[key[0]]=section_info_s[0].split(',')[2].split(' ')[2]
                except IndexError:
                    pass
                                
                try:
                    d[key[1]] =section_info_s[0].split(',')[1].split(' ')[2]
                except IndexError:
                    pass
                                    
                try:    
                    d[key[2]] =section_info_s[0].split(',')[1].split(' ')[4]    
                except IndexError:
                    pass
                    
                try:
                    d[key[3]]=arttitle_s[i]
                except IndexError:
                    pass
                
                try:
                    d[key[4]]=aut[i]
                except IndexError:
                    pass
                
                try:
                    d[key[5]]=keywords1[i]
                except IndexError:
                    pass
                
                try:
                    d[key[6]]=abstract_s[i]
                except IndexError:
                    pass
                
                p.append(d)
                a=url_n1.split('isre/')[1] + '/' + "article%d" % (i+1)
                D[a] = p[i]
            
            
        
        except NoSuchElementException:
            print(driver.current_url,' this page no longer exists')
        
        time.sleep(np.random.randint(1,10))
        count = count+1
        driver.close()
    v = v + 1

'''create json with output it to file '''    
with open('full.json','w') as outfile:
    json.dump(D, outfile)    





        