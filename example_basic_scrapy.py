#Objetivo: Scrapy que descarga imagenes de un sitio, en este caso https://www.pexels.com/
#Autor: Gabriel Ramirez T
#Fecha 2019-06-09
import requests
from bs4 import BeautifulSoup
import sys
from urllib.request import urlretrieve

def run():

    response            = requests.get('https://www.pexels.com/')

    soup                = BeautifulSoup(response.content,'html.parser')

    for link in soup.find_all('img'):

        image_container= link["src"]

        image_url           = image_container

        image_name          = image_url.split('/')[-1]

        r = requests.get(image_container)

        with open(image_name, "wb") as code:

            code.write(r.content)

            code.close

if __name__=='__main__':
    run()
