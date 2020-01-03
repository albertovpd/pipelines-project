# Pipelines-project
This program receives inputs through terminal, deliver custom graphs and save it in PDF. 
I have been working with datasets and performing web scraping to show the mean price of electricity per year, the mean price one day ahead per year (due to forecast changes and other factors the price of energy one day ahead is important, affects the price the day after) and the rise of minimum salary income. 

- Help and display through terminal
![alt text](https://github.com/albertovpd/pipelines-project/blob/master/output/terminal%20example.png "final result")

- Popup graphs through terminal
![alt text](https://github.com/albertovpd/pipelines-project/blob/master/output/output%20example.png "terminal")

- Web scraping
![alt text]( "web enriching")

# Introduction:

This is an individual project to comprehend and strengthen:

    - Pipelines.
    - Argparse.
    - Init functions with its help and several arguments.
    - Fundamentals of web scraping.
    

# Libraries:

        uncertain_panda,pandas, numpy, requests, bs4, matplotlib, sys, argparse,subprocess.


# Description and results:

The main idea was to create a huge dataset relating price of electric energy depending of its source (oil, coal, renewables), per hour, with the climate historic. It was hard to find a for free weather API for all request I need to perform, so finally, I did the following:

- Take all registers of price of energy per hour within the last 4 years (I could not find a bigger dataset with this info).
    https://www.kaggle.com/nicholasjhana/energy-consumption-generation-prices-and-weather

- Perform the mean  per year <b>with its associated uncertainty</b>, in order to have a real measure.

- Web scraping: relate this 4 years of average electric price with the average salary in Spain.
    https://datosmacro.expansion.com/mercado-laboral/salario-medio/espana

- Pipelines. Save related functions in the same script and call them when necessary.
    - From main.py: calling functions in other scripts, creating my function to work through terminal.
    - From web_enriching: performing web scraping.
    - From processing_functions.py: cleaning the dataset, calling functions from the file web_enriching.py to enrich my dataset, developing my key function, the ultimate one which takes arguments through terminal (it is called from main.py and work with the input arguments plotting columns of the dataset).

### How it works:

In case you are using Python 3, from /src:

    python3 main.py -a "first optional argument" -b "second optional argument"

### Accomplished goals:

- Develop an effective pipeline with clean code.
- Run a script with different optional parameters through terminal.
- Understand the basics of web scraping.
- Show uncertainties associated with measures or statistic methods.
- Display graphs through terminal.
- Save your plots

# Improvements:

- Enlarge the dataset.
- Apply ML to predict future prices.
- Finish the graph results with proper label and legends.
- Send by mail the asked results.
