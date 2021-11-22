import requests
from bs4 import BeautifulSoup

c = requests.get('https://www.coingecko.com/en/coins/ravencoin/usd')

soup = BeautifulSoup(c.content, "html.parser")
raven_coin_value = soup.find_all("span", {
    "class": "no-wrap", "data-coin-symbol": "rvn", "data-target": "price.price"})[0].text

one_day_trading_vol = soup.find_all(
    "span", {"class": "no-wrap", "data-target": "price.price", "data-no-decimal": "false"})[0].text

circulating_supply = str(soup.find_all("span", {
    "class": "tw-text-gray-900 dark:tw-text-white tw-float-right tw-font-medium tw-mr-1"})[0].text).strip()

total_supply = str(soup.find_all("span", {
    "class": "tw-text-gray-900 dark:tw-text-white tw-float-right tw-font-medium tw-mr-1"})[1].text).strip()
