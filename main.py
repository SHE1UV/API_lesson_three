import os
from urllib.parse import urlparse
import argparse
import requests
from dotenv import load_dotenv

def shorten_link_url(headers, url):
    check_body = requests.get(url)
    check_body.raise_for_status()
    body = {
        "long_url": url
    }
    response = requests.post("https://api-ssl.bitly.com/v4/shorten/", headers=headers, json=body)
    return response.json()['id']

def count_clicks(headers, short_link):
    url_sum = f"https://api-ssl.bitly.com/v4/bitlinks/{short_link}/clicks/summary"
    response = requests.get(url_sum, headers=headers)
    return response.json()['total_clicks']

def is_bitlink(headers, bitlink):
    bitl = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}"
    response = requests.get(bitl, headers=headers)
    return response.ok

def main():
    apikey_bitly = os.getenv('APIKEY_BITLY')
    headers = {
        "Authorization": f"Bearer {apikey_bitly}",
    }
    parser = argparse.ArgumentParser(description='Сокращает ссылки и выводит количество переходов по ней')
    parser.add_argument('link', help='Введите ссылку:')
    args = parser.parse_args()
    print(args.link)

    parse_link = urlparse(args.link)
    mybitlink = f"{parse_link.netloc}{parse_link.path}"
    try:
        if is_bitlink(headers, mybitlink):
            print(count_clicks(headers, mybitlink))
        else:
            print(shorten_link_url(headers, args.link))
    except requests.exceptions.HTTPError as error:
        print("неверная ссылка.", error)

if __name__ == "__main__":
    main()
