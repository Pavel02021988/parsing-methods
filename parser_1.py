import requests
from bs4 import BeautifulSoup
import csv
# парсинг и очистка данных, запись в csv

def get_html(url):
    r = requests.get(url)
    return r.text

def clean(s):
    r = s.split(' ')[0]
    return r.replace(',', '')

def write_csv(data):
    with open('plugin.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                         data['url'],
                         data['rating']))

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    popular = soup.find_all('section')[3]
    plugins = popular.find_all('article')
    for plugin in plugins:
        name = plugin.find('h2').text
        url = plugin.find('h2').find('a').get('href')
        r = plugin.find('span', class_='rating-count').find('a').text
        rating = clean(r)
        data = {'name':name,
                'url':url,
                'rating':rating}
        write_csv(data)



def main():
    url = 'https://wordpress.org/plugins/'
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()
