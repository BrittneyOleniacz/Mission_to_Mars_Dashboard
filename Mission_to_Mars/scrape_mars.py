from bs4 import BeautifulSoup as soup
from splinter import Browser
import os;
os.environ["PATH"] += os.pathsep + 'C:\\Users\\britt\\Desktop\\GIT_SUBMIT\\Web-Scraping-Challenge';

import time
from selenium import webdriver
# options.setBinary("~\\codespace\\DataViz-Online\\01-Assignments\\10-Mission-to-Mars\\Solution\\chromedriver_win32");
driver = webdriver.Chrome()
#'C:\\Users\\britt\\Desktop\\GIT_SUBMIT\\Web-Scraping-Challenge'
# Optional argument, if not specified will search path.
driver.get('http://www.google.com/');
time.sleep(5)
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) 
driver.quit()

executable_path = {'executable_path': 'C:\\Users\\britt\\Desktop\\GIT_SUBMIT\\Web-Scraping-Challenge'}
browser = Browser('chrome')

url = 'https://mars.nasa.gov/news/'
browser.visit(url)
time.sleep(5)
html = browser.html
news_soup = soup(html, 'html.parser')

all_titles = news_soup.find_all('div', class_ = 'content_title')
all_titles

news_title = all_titles[3].get_text()
news_title

article_teaser = news_soup.find_all('div', class_ = 'article_teaser_body')
news_teaser = article_teaser[3].get_text()
news_teaser

import pandas as pd
url = https://space-facts.com/mars/
mars_fact = pd.read_html(url)[0].to_html


# ### Mars Hemispheres
url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser(visit(url))

hemisphere_image_urls_title = browser.find_by_xpath('//h3')
for h in hemisphere_image_urls_title:
    print(h.text)

hemisphere_image_urls_title_list = [h.text for h in hemisphere_image_urls_title]
hemisphere_image_urls_title_list

parent = browser.find_by_xpath('//h3/parent::a')
len(parent)
for p in parent:
    print(p.parent)
for t in parent:
    print(p.['href'])

hemisphere_image_urls = browser.find_by_xpath('//a[text()="Sample"]')
hemisphere_image_urls [0]['href']
import time
url=
browser.vist(url)
time.sleep(5)
hemisphere_image_urls = []
not_tied_to_the_browser = [1['href'] for l in browser.find_by_xpath('//h3/parent::a')]
for link in not_tied_to_the_browser:
    browser.visit(link)
    time.sleep(1)
    hemisphere_image_urals.append(browser.find_by_xpath('//a[text()="Sample"]')[0]["href"])
    
print(hemisphere_image_urls)
print(hemisphere_image_urls_title)

list(zip(hemisphere_image_urls,hemisphere_image_urls_title))
[{'title':title, 'img_url':link} for title, link in zip(hemisphere_image_urls,hemisphere_image_urls_title)]
output = {
    'news_title': news_title,
    'news_pic': news_picture,
    'featured':featured_image_url,
    'Mars_facts':Mars_facts,
    'hemisphere_image_urls':hemisphere_image_urls
}

browser.quit()

return output 
print(scrape())

