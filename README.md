# pipelines-project
Creation of a .py file that receive inputs through terminal and deliver custom graphs.

It is shown some .png results on "output" folder.
The main .py file is in "src" folder

## Motivation

My main idea was to create a huge dataset relating price of electric energy depending of its source (oil, coal, renewables), per hour, with the climate historic. It was hard to find a for free weather API, so finally, I did the following:

- take all registers of price of energy per hour within the last 4 years (I could not find a bigger dataset with this info)
    https://www.kaggle.com/nicholasjhana/energy-consumption-generation-prices-and-weather
- perform the mean  per year with its associated uncertainty, in order to have a real measure
- web scraping: relate this 4 years of average electric price with the average salary in Spain
    https://datosmacro.expansion.com/mercado-laboral/salario-medio/espana
- pipelines. Save related functions in the same .py and call them when necessary
    - from main.py: calling functions storaged in other .py files, creating my function to work throgh terminal.
    - from web_enriching: performing web scraping
    - from processing_functions.py: cleaning the dataset, calling functions from the file web_enriching.py to enrich my dataset, developing my key function, the ultimate one which takes arguments through terminal (it is called from main.py and work with the input arguments plotting columns of the dataset) 
    
## Accomplished goals
- Understand the basics of pipelines and web scraping.
- Show uncertainties associated with measures or statistic methods
- Coherent pipelines
- Display graphs through terminal

## Future improvements
- The lack of size of my final dataset must be solved, in order to create accurate predictions or display conclusive graphs
- create a PDF with the inputs selected and send it by mail 