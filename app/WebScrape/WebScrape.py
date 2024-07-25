
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

class WebScrape:
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    def read_links(self, element):
        links = element.find_elements(By.TAG_NAME, 'a')
        hrefs = {}
        for link in links:
            hrefs = link.get_attribute('href')
        return hrefs
    

    def get_header (self):
        header = self.driver.find_element(By.TAG_NAME, 'h1')
        return header.text


    def info_box(self):
        data = []
        info_box = self.driver.find_element(By.CLASS_NAME, 'infobox').find_elements(By.TAG_NAME, 'tr')
        
        for infos in info_box:
            columns = infos.find_elements(By.XPATH, './/td | .//th')

            for column in columns:
                content_elements = column.find_elements(By.XPATH, './/td[@scope="row"]')
                content_text = [elem.text for elem in content_elements]
                hyperlinks = self.read_links(column)
                
                cell_data = {
                    "raw_text": column.text,
                    "hyperlinks": hyperlinks ,
                    "text_content": {
                        "title": content_text ,
                        "content": "" 
                    }
                }

    
                data.append(cell_data)
        return data
    

    def article(self):
        data = []   
        raw_article = self.driver.find_elements(By.TAG_NAME, 'p')
        captions = self.driver.find_elements(By.TAG_NAME, 'h2')
    
        for article, caption in zip(raw_article, captions):
            hyperlinks = {}
            links = article.find_elements(By.TAG_NAME, 'a')
            for link in links:
                link_text = link.text
                link_url = link.get_attribute('href')
                hyperlinks[link_text] = link_url
            
            paragraph_data = {
                caption.text: [
                    {
                        "Type": article.tag_name,
                        "Text_content": article.text,
                        'hyperlinks': hyperlinks
                    }
                ]
            }
            data.append(paragraph_data)

        return data
    

