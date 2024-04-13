import selenium
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import undetected_chromedriver as uc
import time
import csv


# m using headers to misslead the website so it thinks that the request is coming from a browser (real person)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

# proxies : i may not use them to make it quick but still gotta mention that i can use them to flex my knwodlge ak chayef hada ana mchi copilot)
# haka yji al proxy : options = Options() , proxy_server_url = "157.245.97.60" , options.add_argument(f'--proxy-server={proxy_server_url}')




url = 'https://fatabyyano.net/'





service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
html_doc = requests.get(url, headers=headers)
driver.get(url)


html_doc = driver.page_source
soup = BeautifulSoup(html_doc, 'lxml')


driver.close()
driver.quit()



for page in range(5):
    url = f'https://fatabyyano.net/page/{page+1}/'
    html_doc = requests.get(url, headers=headers)
    soup = BeautifulSoup(html_doc.content, 'html.parser')


h2_elements = soup.find_all('h2', class_='w-post-elm post_title usg_post_title_1 has_text_color entry-title color_link_inherit')
a_elemnts = [h2.find('a') for h2 in h2_elements]
time_elemnts = soup.find_all('time', class_='w-post-elm post_date usg_post_date_1 has_text_color entry-date published')
category_elements = soup.find_all('span', class_='w-btn-label')




titles = [h2.text for h2 in h2_elements]
times = [time['datetime'] for time in time_elemnts]
categories = [category.text for category in category_elements]
links = [a['href'] for a in a_elemnts]


# Write the titles to a CSV file
with open('1-Fatabayano.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['title', 'time','category'])  # Write the column names
    writer.writerows([[title, time, category] for title, time,category in zip(titles, times, categories)])  # Write the data
  
  
#wpb_wrapper
#w-post-elm post_content without_sections