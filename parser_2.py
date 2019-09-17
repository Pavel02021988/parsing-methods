import requests
from bs4 import BeautifulSoup
import csv

# Парсинг табличных данных и запись в csv

def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('cmc.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow([data['name'],
                         data['price'],
                         data['url'],
                         data['symbol']])


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')

    trs = soup.find('table', id='currencies').find('tbody').find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')
        name = tds[1].find('a', class_='currency-name-container').text
        symbol = tds[1].find('a').text
        url ='https://coinmarketcap.com' + tds[1].find('a').get('href')
        price = tds[3].find('a').get('data-usd')

        data = {'name': name,
                'symbol': symbol,
                'url': url,
                'price': price}
        write_csv(data)





def main():
    url = 'https://coinmarketcap.com/'

    get_data(get_html(url))







if __name__ == '__main__':
    main()