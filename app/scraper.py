import requests
from bs4 import BeautifulSoup

headers = {
  'authority': 'www.amazon.pl',
  'cache-control': 'max-age=0',
  'rtt': '50',
  'downlink': '5.9',
  'ect': '4g',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'sec-fetch-site': 'none',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-user': '?1',
  'sec-fetch-dest': 'document',
  'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
}

def check_price(url):
  try:
    page_content = requests.get(url, headers=headers, allow_redirects=False)
    assert page_content.status_code == 200, "Invalid page"
    soup = BeautifulSoup(page_content.content, 'html.parser')
    price_box = soup.find("span", {"class":"a-price aok-align-center"})
    price_text = price_box.find("span", {"class":"a-offscreen"}).text
  except:
    return None
  return price_text


def find_image(url):
  try:
    page_content = requests.get(url, headers=headers, allow_redirects=False)
    assert page_content.status_code == 200, "Invalid page"
    soup = BeautifulSoup(page_content.content, 'html.parser')

    image_box = soup.find("img", {"id":"landingImage"})
    image_url = image_box['src']
  except:
    return
  return image_url
