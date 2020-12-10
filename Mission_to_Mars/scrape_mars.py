from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time

def myScrape():

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')
    all_titles = news_soup.find_all('div', class_ = 'content_title')
    news_title = all_titles[1].get_text()
    article_teaser = news_soup.find_all('div', class_ = 'article_teaser_body')
    news_teaser = article_teaser[1].get_text()

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(1)
    featured_image_url = 'https://www.jpl.nasa.gov' + browser.find_by_xpath('//article[@class="carousel_item"]')[0]['style'].split('"')[1]

    url = 'https://space-facts.com/mars/'
    browser.visit(url)
    time.sleep(1)
    mars_facts = pd.read_html(url)[0].to_html

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    time.sleep(1)
    hemisphere_image_urls_title = browser.find_by_xpath('//h3')
    hemisphere_image_urls_title_list = [h.text for h in hemisphere_image_urls_title]

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    time.sleep(1)
    hemisphere_image_urls = []
    not_tied_to_browser = [n['href'] for n in browser.find_by_xpath('//h3/parent::a')]
    for link in not_tied_to_browser:
        browser.visit(link)
        time.sleep(1)
        hemisphere_image_urls.append(browser.find_by_xpath('//a[text()="Sample"]')[0]['href'])

    hemisphere_image_urls = [{'title':title,'img_url':link} for title, link in zip(hemisphere_image_urls_title_list,hemisphere_image_urls)]

    output = {
        'news_title' : news_title,
        'news_teaser': news_teaser,
        'featured': featured_image_url,
        'Mars_facts': mars_facts,
        'hemisphere_image_urls': hemisphere_image_urls}

    browser.quit()

    return output
