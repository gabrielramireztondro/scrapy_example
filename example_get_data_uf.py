#Objetivo: Scrapy que extrae
#Autor: Gabriel Ramirez T
#Fecha 2019-06-09
import requests
from bs4 import BeautifulSoup
import sys
from urllib.request import urlretrieve
import time

def run(dia,mes, anio):

    mes_letter='mes_{0}'.format(mes)

    url='http://www.sii.cl/valores_y_fechas/uf/uf{0}.htm'.format(anio)

    response            = requests.get(url)

    soup                = BeautifulSoup(response.content,'html.parser')

    mes_container       = soup.find(id=mes_letter)

    dia_container       = mes_container.find_all('tr')
    exists=0
    for i, valor in enumerate(dia_container):
        if exists==1:
            break
        for ii, valor in enumerate(valor):
            if exists==0:
                if str(valor).strip()=='<th width="40"><strong>{0}</strong></th>'.format(dia):
                    exists=1
                    print('Encontrado')
            elif exists==1 and str(valor).strip()!='':
                valor_uf=str(valor).replace('<td width="200">','')
                valor_uf=valor_uf.replace('</td>','')
                print('El valor de la Uf del día {} de {} del {} es {}'.format(dia,mes,anio,valor_uf))
                break




if __name__=='__main__':

    meses=dict()
    meses['enero'] = '1'
    meses['febrero'] = '2'
    meses['marzo'] = '3'
    meses['abril'] = '4'
    meses['mayo'] = '5'
    meses['junio'] = '6'
    meses['julio'] = '7'
    meses['agosto'] = '8'
    meses['septiembre'] = '9'
    meses['octubre'] = '10'
    meses['noviembre'] = '11'
    meses['diciembre'] = '12'

    dia=time.strftime("%d")
    mes=time.strftime("%m")
    anio=time.strftime("%Y")
    mes_letter=""

    for k,v in meses.items():

        if int(v)==int(mes):

            mes_letter=k


    run(dia,mes_letter,anio)
