import requests
from bs4 import BeautifulSoup
import pandas as pd

def web_scraping():
    url="https://datosmacro.expansion.com/mercado-laboral/salario-medio/espana"

    res = requests.get(url)
    html = res.text
    html[:20]
    salary = BeautifulSoup(html, 'html.parser')

    repos = salary.select('tr')

    year=[]

    for x in repos[1:5]:
        for i in x:
            i=str(i)
            year.append(i)

    dates=[]
    incomes=[]
    for x in year[0::3]:
        dates.append(x[-9:-5])
    for x in year[1::3]:
        incomes.append(x[-12:-6])
    spain=pd.DataFrame(dates,incomes)

    return incomes