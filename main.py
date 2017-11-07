from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver')
driver.get("https://tjmaxx.tjx.com/store/jump/product/Western-Toe-Heel-Booties/1000263516?colorId=NS2857147&pos=1:1&Ntt=western%20toe%20heel%20booties")

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

available_sizes = []

for size in soup.find_all("span", class_="option-name"):
    if size.contents[0] == '8':

print(available_sizes)

driver.quit()
