from bs4 import BeautifulSoup
from requests import get
import logging
import datetime
import smtplib

from config import config
from base64 import b64decode

now = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
logfile = f"gambody-{now}"

logging.basicConfig(filename=logfile, encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger(__name__)

def getSoup(url):
    result = get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    return soup

def divs(soup, className):
    return soup.body.find_all('div', class_=className)

def getObjectLinks(soup):
    return [link['href'] for link in soup.find_all('a', class_='txt to-details')]

def nextPage(soup):
    link = soup.body.find_all('a', class_='active')
    nextPage = int(link[0].text) + 1
    return f"/page/{nextPage}/sort/default"

def resultMail(hits):
    sender = config['sender']
    receivers = config['receivers']
    subject = "Happy Monday Gambody Deals"
    body = f"""
Happy Monday Discount Deals:

https://www.gambody.com{hits[0]}
https://www.gambody.com{hits[1]}
    """
    payload = f"From: {sender}\nTo: {receivers}\nSubject: {subject}\n\n{body}"
    try:
        server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server_ssl.ehlo()
        server_ssl.login(config['username'], b64decode(config['password']).decode('utf-8').strip())
        server_ssl.sendmail(sender, receivers, payload)
        server_ssl.close()
        logger.debug(f"Mail sent...")
    except ValueError as e:
        logger.debug(f"Sending mail failed: {e}")


if __name__ == '__main__':
    url = 'https://www.gambody.com'
    page = "/page/1/sort/default"
    links = []
    magicLink = "https://www.gambody.com/blog/happy-monday-update/"
    while True:
        lastPage = page
        soup = getSoup(f"{url}/search/{page}")
        links+=getObjectLinks(soup)
        page = nextPage(soup)
        if lastPage == page:
            break

    hits = []
    for link in links:
        logger.debug(link)
        result = get(f"{url}{link}")
        if magicLink in result.text:
            hits+=[link]
            logger.debug(f"Treffer: {link}")

    if hits:
        resultMail(hits)