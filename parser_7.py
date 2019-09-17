import requests
from bs4 import BeautifulSoup
from random import choice

# Парсинг с помощью proxy

def get_html(url):
    p = get_proxy()
    proxy = {p['shcema']: p['address']}
    r = requests.get(url, proxies=proxy, timeout=5)
    return r.json()['origin']

def get_proxy():
    html = requests.get('https://free-proxy-list.net/').text
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table', id='proxylisttable').find_all('tr')[1:11]
    proxies = []
    for tr in trs:
        tds = tr.find_all('td')
        ip = tds[0].text.strip()
        port = tds[1].text.strip()
        shcema = 'https' if 'yes' in tds[6].text.strip() else 'http'
        proxy = {'shcema': shcema, 'address': ip + ":" + port}
        proxies.append(proxy)
    return choice(proxies)

def main():
    url = 'http://httpbin.org/ip'
    print(get_html(url))



if __name__ == '__main__':
    main()