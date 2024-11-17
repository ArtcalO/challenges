from bs4 import BeautifulSoup
from selenium import webdriver
import sys
import locale
from fake_useragent import UserAgent
import platform
import random
import time



def get_current_os():
    if(platform.system()=="Darwin"):
        return "macos"
    return platform.system().lower()

# headers pour montrer que c'est un navigateur valide
def get_random_headers():
    ua = UserAgent(browsers=['chrome'], os=get_current_os())
    return ua.random
    
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    #     'Referer': 'https://www.google.com/',
    #     'Accept-Language': "",
    #     'Accept-Encoding': "",
    #     'Connection': ""
    # }

def requests_delay():
    sleep_time = random.uniform(1, 10)
    time.sleep(sleep_time)


def analyse_site(url):

    # Configuration de Selenium 
    options = webdriver.ChromeOptions()

    #ajout des headers
    headers = get_random_headers()
    options.add_argument(f'user-agent={headers}')

    # Initialiser le navigateur Chrome avec les options configurées
    driver = webdriver.Chrome(options=options)

    driver.get(url=url)

    # ajout d'un sleep avant de parser le html
    requests_delay()


    # Récupérer le contenu généré par JavaScript
    html_content = driver.page_source

    print(html_content)

    # Fermer le navigateur
    driver.quit()


    # Utiliser BeautifulSoup pour parser le code HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    requests_delay()
    results = soup.find_all("div", class_="Nv2PK THOPZb CpccDe")
    scrapped_items = []
    for result in results:
        header = result.find("div", class_="qBF1Pd fontHeadlineSmall").text.strip()
        etoiles = result.find("span", class_="MW4etd").text.strip()
        nb_avis = result.find("span", class_="UY7F9").text.strip()
        location = result.select("div.W4Efsd > span:nth-child(2) > span:nth-child(2)")
        print([x for x in location])
        data = {
            "header":header,
            "etoiles":etoiles,
            "nb_avis":nb_avis,
            "location":location
        }
        scrapped_items.append(data)

    print(scrapped_items)


info = analyse_site("https://www.google.com/maps/search/restaurants/")