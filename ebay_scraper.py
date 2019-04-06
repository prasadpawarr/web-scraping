from bs4 import BeautifulSoup
import requests

def get_page(url):
    response = requests.get(url)
    if not response.ok:
        print('Server responded: ',response.status_code)
        raise SystemExit
    else:
        soup = BeautifulSoup(response.text, 'lxml')
        return soup


def get_single_page_data(soup):
    collection = []
    links = soup.find_all('a', class_="s-item__link")
    for link in links:
        url = link['href']
        sp = get_page(url)
        get_data(sp, collection)


def get_data(soup, collection):
    try:
        title = soup.find(
            'span', attrs={'class': 'u-dspn', 'id': 'vi-lkhdr-itmTitl'}).text
    except:
        title = ''
    
    try:
        price = soup.find('span', itemprop='price').text
    except:
        price = ''
    
    try:
        # items_sold = soup.find('div', id='why2buy').find('span', class_='w2b-sgl').text
        items_sold = soup.find('a', class_="vi-txt-underline").text
    except:
        items_sold = 'NULL'

    data = {
        'title': title, 
        'price': price, 
        'items_sold': items_sold 
    }
    print(data)
    print()

def main():
    url = 'https://www.ebay.com/sch/i.html?_nkw=mens+watches&_pgn=1'
    get_single_page_data(get_page(url))


if __name__ == "__main__":
    main()
