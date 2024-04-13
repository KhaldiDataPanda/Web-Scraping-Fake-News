
import requests
from bs4 import BeautifulSoup
import csv


# m using headers to misslead the website so it thinks that the request is coming from a browser (real person)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

# proxies : i may not use them to make it quick but still gotta mention that i can use them to flex my knwodlge ak chayef hada ana mchi copilot)
# haka yji al proxy : options = Options() , proxy_server_url = "157.245.97.60" , options.add_argument(f'--proxy-server={proxy_server_url}')




url = 'https://fatabyyano.net/'
all_data = []


for page in range(20):
    url = f'https://fatabyyano.net/page/{page+1}/'
    html_doc = requests.get(url, headers=headers)
    soup = BeautifulSoup(html_doc.content, 'html.parser')

    
    h2_elements = soup.find_all('h2', class_='w-post-elm post_title usg_post_title_1 has_text_color entry-title color_link_inherit')

    for h2 in h2_elements:
        
        link = h2.find('a')['href']
        link_html = requests.get(link, headers=headers)
        link_soup = BeautifulSoup(link_html.content, 'html.parser')

        #saving link_soup 
        with open('link_soup.html', 'w', encoding='utf-8') as file:
            file.write(str(link_soup))
            file.close()
        
        
        div1 = link_soup.find('blockquote')
        if div1 is not None:
            div1 = div1.text.strip()
        else :
            div1 = ''
        
        
        div2 = link_soup.select_one('#page-content > section.l-section.wpb_row.us_custom_81f21468.height_auto > div > div > div.vc_col-sm-8.wpb_column.vc_column_container > div > div > div.w-post-elm.post_content.without_sections > div:nth-child(6)')
        if div2 is not None:
            div2 = div2.text.strip()
        else:
            div2 = ''
        
        
        div3 = link_soup.select_one('#page-content > section.l-section.wpb_row.us_custom_81f21468.height_auto > div > div > div.vc_col-sm-8.wpb_column.vc_column_container > div > div > div.w-post-elm.post_content.without_sections > div:nth-child(13)')
        if div3 is not None:
            div3 = [a['href'] for a in div3.find_all('a')]
        else:
            div3 = ''

        title = h2.text.strip()
        time = soup.find('time', class_='w-post-elm post_date usg_post_date_1 has_text_color entry-date published')['datetime']
        category = soup.find('span', class_='w-btn-label').text.strip()


        all_data.append([title, time, category,link,div1,div2,div3])








with open('1-Fatabayano.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Time', 'Category','Link','Claim' ,'Investigation', 'SourcesLinks'])
    writer.writerows(all_data)