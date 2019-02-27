from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

# this is an example of scraping video card info from new egg
# url target
scrape_url = 'https://www.newegg.com/global/au-en/Video-Cards-Video-Devices/Category/ID-38'
# open connection
uclient = ureq(scrape_url)
page_html = uclient.read()
uclient.close()

filename = 'products.csv'
f = open(filename, 'w')

headers = 'brand, product_name\n'

f.write(headers)

# html parsing
page_soup = soup(page_html, 'html.parser')

containers = page_soup.find_all('div', {'class': 'item-container'})

for container in containers:
    brand = container.find('div', {'class': 'item-branding'}).img['title']
    product_name = container.find('a', {'class': 'item-title'}).text
    f.write(f'{brand}, {product_name.replace(",", "|")}\n')

f.close()