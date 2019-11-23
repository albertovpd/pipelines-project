# Pipelines-project
This .py file receives inputs through terminal and deliver custom graphs. I have been researching trough datasets and web scraping to show the mean price of electricity per year, the mean price one day ahead per year (due to forecast circunstances and other factors the price of energy one day ahead is important and affects the price the day after) and the rise of minimus salary income. 

- Help and display through terminal
![alt text](https://github.com/albertovpd/pipelines-project/blob/master/output/terminal%20example.png "final result")

- Popup graphs trhrough terminal
![alt text](https://github.com/albertovpd/pipelines-project/blob/master/output/output%20example.png "terminal")

## Motivation
My main idea was to create a huge dataset relating price of electric energy depending of its source (oil, coal, renewables), per hour, with the climate historic. It was hard to find a for free weather API, so finally, I did the following:

- Take all registers of price of energy per hour within the last 4 years (I could not find a bigger dataset with this info).
    https://www.kaggle.com/nicholasjhana/energy-consumption-generation-prices-and-weather
- Perform the mean  per year with its associated uncertainty, in order to have a real measure.
- Web scraping: relate this 4 years of average electric price with the average salary in Spain.
    https://datosmacro.expansion.com/mercado-laboral/salario-medio/espana
- Pipelines. Save related functions in the same .py and call them when necessary
    - From main.py: calling functions storaged in other .py files, creating my function to work throgh terminal.
    - From web_enriching: performing web scraping
    - From processing_functions.py: cleaning the dataset, calling functions from the file web_enriching.py to enrich my dataset, developing my key function, the ultimate one which takes arguments through terminal (it is called from main.py and work with the input arguments plotting columns of the dataset) 
    
## Accomplished goals
- Understand the basics of pipelines and web scraping.
- Show uncertainties associated with measures or statistic methods.
- Coherent pipelines.
- Display graphs through terminal.

## Future improvements
- The lack of size of my final dataset must be solved, in order to create accurate predictions or display conclusive graphs.
- Finish the graph results with proper label and legends.
- Create a PDF with the inputs selected and send it by mail. 
