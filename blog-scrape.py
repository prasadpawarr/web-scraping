'''
scrapes the title, summary and blog-link
and stores it in a csv format

- uses beautifulsoup4
  and lxml parser

'''

from bs4 import BeautifulSoup
import requests
import csv

src = requests.get('https://skintdad.co.uk/').text
soup = BeautifulSoup(src, 'lxml')

csv_file = open('blog-scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title', 'summary', 'link'])



for article in soup.find_all('article'):
    title = article.header.h2.text.strip()
    # print(title)
    
    para = article.find('div', class_='entry-content').p.text.strip()
    # print(para)
    
    article_link = article.find('div', 'entry-content').a['href']
    # print(article_link, end="\n")

    csv_writer.writerow([title, para, article_link])


csv_file.close()