from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.get("https://tjmaxx.tjx.com/store/jump/product/Western-Toe-Heel-Booties/1000263516?colorId=NS2857147&pos=1:1&Ntt=western%20toe%20heel%20booties")

sizes = driver.find_elements_by_class_name("option-name")

for available in sizes:
    # size = available.getAttribute("innerHTML")
    print(available)

driver.quit()
