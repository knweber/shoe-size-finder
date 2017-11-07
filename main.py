from selenium import webdriver
from bs4 import BeautifulSoup
import smtplib

def getSizes():
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://tjmaxx.tjx.com/store/jump/product/Western-Toe-Heel-Booties/1000263516?colorId=NS2857147&pos=1:1&Ntt=western%20toe%20heel%20booties")

    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")

    available_sizes = []

    for size in soup.find_all("span", class_="option-name"):
        if size.contents[0] == '8':
            sendEmail()

    print(available_sizes)

    driver.quit()

def sendEmail():
    user = "user@gmail.com"
    pswrd = "mypassword"
    message = "Your size is available! Go to 'https://tjmaxx.tjx.com/store/jump/product/Western-Toe-Heel-Booties/1000263516?colorId=NS2857147&pos=1:1&Ntt=western%20toe%20heel%20booties' now!"
    server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 587)
    server_ssl.ehlo()
    server_ssl.login(user,pswrd)
    server_ssl.sendmail(user,user,message)
    server_ssl.close()
    print "Email sent!"

if __name__ == "__main__":
    getSizes()
