# 📘 Day 22: - 30DaysOfPython Challenge by Swift Cyberwatch
## Python Web Scraping
### What is Web Scrapping
'''
The internet is full of huge amount of data which can be used for different purposes. To 
collect this data we need to know how to scrape data from a website.
Web scraping is the process of extracting and collecting data from websites and storing it on 
a local machine or in a database.
In this section, we will use beautifulsoup and requests package to scrape data. The package 
version we are using is beautifulsoup 4.
To start scraping websites you need _requests_, _beautifoulSoup4_ and a _website_.
'''
# pip install requests
# pip install beautifulsoup4
'''


To scrape data from websites, basic understanding of HTML tags and CSS selectors is needed. We 
target content from a website using HTML tags, classes or/and ids.
Let us import the requests and BeautifulSoup module

'''
import requests
from bs4 import BeautifulSoup

# Let us declare url variable for the website which we are going to scrape.

import requests
from bs4 import BeautifulSoup
url = 'https://www.swiftcyberwatch.com/scw'
# Lets use the requests get method to fetch the data from url
response = requests.get(url)
# lets check the status
status = response.status_code
print(status) # 200 means the fetching was successful

# Using beautifulSoup to parse content from the page

import requests
from bs4 import BeautifulSoup
url = 'https://www.swiftcyberwatch.com/scw'
response = requests.get(url)
content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print(soup.title) # <title>Swift Cyberwatch</title>
print(soup.title.get_text()) # Swift Cyberwatch
print(soup.body) # gives the whole page on the website with the html tags
print(soup.body.get_text()) # gives the whole text on the page without the html tags
print(response.status_code)
# If you have a text field within a table, you can target that field.
tables = soup.find_all('table', {'cellpadding':'3'})
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
table = tables[0] # the result is a list, we are taking out data from it
for td in table.find('tr').find_all('td'):
    print(td.text)

'''
If you run this code, you can see that the extraction is half done. You can continue doing it 
because it is part of exercise 1.
For reference check the [beautifulsoup 
documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start)
'''