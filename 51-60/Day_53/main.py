import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

ZILLOW = "ZILLOW SEARCH ADDRESS"

ACCEPT_LANGUAGE = "AGENT LANGUAGE" 
USER_AGENT = "USER AGENT"

HEADERS = {
    "Accept-Language": ACCEPT_LANGUAGE,
    "User-Agent": USER_AGENT
}

CHROME_DRIVER_PATH = "CHROME DRIVER"
FORM = "FORM ADDRESS TO FILL"


response = requests.get(ZILLOW, headers=HEADERS)
zillow_page = response.text

soup = BeautifulSoup(zillow_page, "html.parser")

all_links_elements = soup.select(".list-card-top a")

all_links = []

for listing in all_links_elements:
    link = listing["href"]

    if "http" not in link:
        all_links.append(f"https://www.zillow.com{link}")
    else:
        all_links.append(link)

all_addresses_elements = soup.select(".list-card-info address")
all_addresses = [address.get_text().split(" | ")[-1] for address in all_addresses_elements]

all_prices_elements = soup.select(".list-card-heading")
all_prices = []

for element in all_prices_elements:

    try:
        price = element.select(".list-card-price")[0].contents[0]
    except IndexError:
        print('Multiple listings for the card')
        price = element.select(".list-card-details li")[0].contents[0]
    finally:
        all_prices.append(price)


driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

for i in range(len(all_links)):
    driver.get(FORM)

    sleep(2)

    address_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

    address_input.send_keys(all_addresses[i])
    price_input.send_keys(all_prices[i])
    link_input.send_keys(all_links[i])

    submit_button.click()


