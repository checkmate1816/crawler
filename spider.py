import urllib.request
from bs4 import BeautifulSoup
import time
from fake_useragent import UserAgent
import smtplib
from email.mime.text import MIMEText

url = 'https://www.avaloncommunities.com/new-york/brooklyn-apartments/ava-fort-greene/#community-unit-listings'
ua = UserAgent()
headers = {"User-Agent":ua.random}
req = urllib.request.Request(url = url,headers=headers)
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
soup = BeautifulSoup(html,"html.parser")
last_price = soup.find(id="pricing-studio-price")

mail_host = 'xxxxxxx'
mail_user = 'xxxxxxx'
mail_pass = 'xxxxxxx'
sender = 'xxxxxxx'
receivers = ['xxxxxxx']


while True:
    headers = {"User-Agent":ua.random}
    req = urllib.request.Request(url = url,headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html,"html.parser")
    price = soup.find(id="pricing-studio-price")
    if price.text != last_price.text:
        smtpobj = smtplib.SMTP(mail_host,25)
        smtpobj.connect(mail_host,25)
        smtpobj.ehlo()
        smtpobj.starttls()
        smtpobj.ehlo()
        smtpobj.login(mail_user,mail_pass)
        message = MIMEText(price.text,'plain','utf-8')
        message['Subject'] = 'AFG studio lowest price'
        message['From'] = sender
        message['To'] = receivers[0]
        smtpobj.sendmail(sender,receivers,message.as_string())
        smtpobj.quit()
        last_price = price

    time.sleep(60)
