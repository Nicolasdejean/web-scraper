#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
import re
import sys
import csv


def url_list(x):
    return {
            'hot': 'https://stackexchange.com/?page=1',
            'real-time': 'https://stackexchange.com/questions?tab=realtime',
            'stackoverflow-new': 'https://stackoverflow.com/questions?page=2&sort=newest'
    }[x]

def populate_question_links(forum = "all", url='https://stackexchange.com/questions?pagesize=50',
                            all_question_links=[]):
     print "url: " + url
     tmp_link = url.split("com")[0]
     tmp_link += "com"

     print "site: " + str(url.find('page='))
     print "urldigit: " + str(url[-1:].isdigit())
     r = requests.get(url) # HTTP request
     html_doc = r.text # Extracts the html
     soup = BeautifulSoup(html_doc, 'lxml') # Create a BeautifulSoup object

     links = []
     print(len(soup.findAll('em')))
     for em in soup.findAll('em'):
         if "No questions found." in em:
             return all_question_links
     for link in soup.find_all('em'):
         print link
     for link in soup.find_all('a'):
        tmp = tmp_link
        url_link = str(link.get('href'))
        if forum != "all":
            if forum not in url_link:
                continue
        if "https://" not in url_link:
            tmp += url_link
            url_link = tmp
        links.append(url_link)
     question_links = [k for k in links if k and 'questions' in k] # Filter links that contain the string 'questions'

     pattern = re.compile('questions/\d') # Create pattern to search for

     question_links = filter(pattern.search, question_links) # Filter links which are questions and also followed by a numerical ID
     question_links = list(set(question_links)) # Remove duplicates

     index = url.find('page=')
     print "nbr: " + url[index + len('page=')]
     if url[index + len('page=')] == '5':
         return all_question_links
     if index != -1:
         url = url.replace(url[index + len('page=')], str(int(url[index + len('page=')]) + 1))
     else:
         return question_links
     print "save_url: " + url
     all_question_links.extend(question_links)
     return(populate_question_links(forum, url, all_question_links))

def find_cat(url):
    return(url.split("https://")[1].split(".")[0])

def get_text(words, url, rm_digits = True, rm_punct = True, pause=False, sleep_max=5):
        if pause == True:
                sleep(randint(1, sleep_max))
        r = requests.get(url)
        html_doc = r.text
        soup = BeautifulSoup(html_doc, 'lxml')

        digit_list = "1234567890"
        punct_list = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        try:
                text = soup.find(attrs={'class':'post-text'}).get_text()
                text = text.replace('\n',' ')
                if rm_punct  == True:
                        for char in punct_list:
                                text = text.replace(char, "")
                if rm_digits == True:
                        for char in digit_list:
                                text = text.replace(char, "")
                for w in words:
                    if w not in text:
                        return
                print "text: " + text
                return(find_cat(url), text)
        except:
                return

def find_url(tab):
        return url_list(tab)

if len(sys.argv) < 4:
        print "usage: research_question.py [tab] [forum] [words...]"
        print "-------------------------------------------"
        print "tab: hot, real-time, ..."
        print "forum: stackoverflow, superuser..."
        print "words: javascript, excel, ..."
        sys.exit(0)

url = find_url(sys.argv[1])
print url

question_links = populate_question_links(sys.argv[2], url)
question = 0

words = []
i = 0
while i < len(sys.argv):
        if i > 2:
                words.append(sys.argv[i])
        i += 1

print words
while question < len(question_links):
    text = get_text(words, question_links[question])
    if text != None:
        print("link nbr " + str(question + 1) + ": " + question_links[question],
               text)
    question += 1
