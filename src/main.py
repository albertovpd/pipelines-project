from uncertain_panda import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import sys
import argparse
import subprocess

data = pd.read_csv ("../input/energy_dataset.csv")

# --- my funcions ---
from processing_functions import working, enriching, decimals, results
from web_enriching import web_scraping
# -------------------


    
def recibeConfig():
    parser = argparse.ArgumentParser(description='''This program creates graphs according to your selection and
    shows a dataset through terminal. --------------------- Giving 2 arguments select from:
     average spanish income (k€), price day ahead (€ MW/h),   price actual(€ MW/h) ------- For 1 arguments: 1. Selecting from the mentioned above you will receive a graph. 2. Selecting 
    from the next items you will receive a dataset: uncertainty ahead, uncertainty actual. ------- Writing wrong 
    the inputs implies you will be asked again for them.''')
    

    parser.add_argument('-a',
                        help='Select: average income, price day ahead, price actual, uncertainty ahead, uncertainty actual',
                        default="price actual"
                        )
    parser.add_argument('-b',
                        help='Select: average income, price day ahead, price actual, uncertainty ahead, uncertainty actual',
                        default=None
                        )
                        
    args = parser.parse_args()
    # print(args)
    return args

def main():
    config=recibeConfig()
    working(data)
    dataset=enriching(data)
    finaldataset=decimals(dataset)

    
    print("1st input: ", config.a, ". 2nd input: ", config.b)
    print("")
    print("Average income (€) \n Other columns ( Measure +- Δ Measure ( € MW / h ) ) ")
    print("")
    print(finaldataset)

    results(finaldataset, config.a, config.b)

if __name__=="__main__":
    main()

