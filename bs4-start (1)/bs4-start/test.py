from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
content = response.text
soup = BeautifulSoup(content, "html.parser")
all_link_elements = soup.select(".ListItem-c11n-8-84-3-StyledListCardWrapper a")
all_links = [link["href"] for link in all_link_elements]
print(f"There are {len(all_links)} links to individual listings in total: \n")
print(all_links)
all_address_elements = soup.select(".ListItem-c11n-8-84-3-StyledListCardWrapper address")
all_addresses = [address.get_text(strip=True).replace(" | ", " ") for address in all_address_elements]
print(all_addresses)
all_price_elements=soup.select(".PropertyCardWrapper span")
all_prices=[price.get_text().replace("/mo"," ").split("+")[0] for price in all_price_elements ]
print(all_prices)
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)
for n in range (len(all_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfwOWKluw5qFC5oAVMFa9LI7ePBSC4oNOUbclFA3ZKMACSv8g/viewform?usp=sf_link ")
    time.sleep(2)
    address=driver.find_element(by=By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price=driver.find_element(by=By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link=driver.find_element(by=By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit=driver.find_element(by=By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    address.send_keys(all_addresses[n])
    price.send_keys(all_links[n])
    link.send_keys(all_links[n])
    submit.click()
