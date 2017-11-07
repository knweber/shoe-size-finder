from selenium import webdriver

driver = webdriver.Chrome('C:/Users/gndweber/Downloads/chromedriver')
driver.get("https://tjmaxx.tjx.com/store/jump/product/Western-Toe-Heel-Booties/1000263516?colorId=NS2857147&pos=1:1&Ntt=western%20toe%20heel%20booties")

sizes = driver.find_elements_by_class_name("option-name")

for size in sizes:
    print(size)

driver.quit()
