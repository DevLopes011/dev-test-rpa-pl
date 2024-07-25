from WebScrape import WebScrape
import json

with open('web_scrape_input.json', 'r') as file:
    data = json.load(file)

url = data['wiki_url']
webScrape = WebScrape(url)


info_box_data = webScrape.info_box()
# print(json.dumps(info_box_data, indent=4, ensure_ascii=False))

header = webScrape.get_header()
# print(header)

article = webScrape.article()
# print(json.dumps(article, indent=4, ensure_ascii=False))

data = {
    "header": header,
    "infobox":  info_box_data,
    "article":  article 
}

json_string = json.dumps(data, indent=4, ensure_ascii=False)
print(json_string)