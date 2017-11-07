from selenium import webdriver
from bs4 import BeautifulSoup
from smtplib import SMTP as SMTP
import schedule
import time

def getSizes():
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://tjmaxx.tjx.com/store/jump/product/Western-Toe-Heel-Booties/1000263516?colorId=NS2857147&pos=1:1&Ntt=western%20toe%20heel%20booties")

    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")

    available_sizes = []

    for size in soup.find_all("span", class_="option-name"):
        if size.contents[0] == '8':
            sendEmail()

    driver.quit()

def sendEmail():
    user = "<YOUR_EMAIL>"
    pswrd = "<YOUR_PASSWORD>"
    message = "Your size is available! Go get those boots."
    conn = SMTP(host="smtp.gmail.com", port=587)
    conn.ehlo()
    conn.starttls()
    conn.ehlo()
    sender = user
    recipient = user
    conn.login(user,pswrd)
    conn.sendmail(sender,recipient,message)
    print("Email sent!")
    conn.close()

schedule.every().day.at("07:00").do(getSizes)

while True:
    schedule.run_pending()
    time.sleep(1)
