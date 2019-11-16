from web_enriching import web_scraping
import matplotlib.pyplot as plt

def working(data):
    null_cols = data.isnull().sum()
    drop_cols = list(null_cols[null_cols > 35000].index)
    data_clean1 = data.drop(drop_cols, axis=1)

    economics = data_clean1[["time","price day ahead", "price actual"]].copy()

    year=[]
    [year.append(int(e[0:4])) for e in economics["time"]]
    
    economics["year"]=year
    economics=economics.drop("time",axis=1)
        
    economics["price day ahead"] = economics["price day ahead"].astype(int)
    economics["price actual"] = economics["price actual"].astype(int)

    economics_values=economics.groupby("year")["price day ahead","price actual"].mean()
    economics_error=economics.groupby("year")["price day ahead","price actual"].unc.mean()
    newnames=economics_error.rename(columns={"price day ahead":"uncertainty ahead", "price actual":"uncertainty actual"})
    eco=economics_values.join(newnames)
    return eco


def enriching(data):    
    # called functions
    incomes=web_scraping()
    eco=working(data)
    # 
    eco["average income"]=incomes[::-1]
    ordered_dataset=eco[["average income", "price day ahead", "price actual","uncertainty ahead","uncertainty actual"]]
    return ordered_dataset

def decimals(data):
    for x in data.columns[0:3]:
        data["{}".format(x)]=data["{}".format(x)].astype(float)

    return data


def results(dataset, a, b=None):    
        
    if b==None:
        if a not in dataset.columns:
            a=input("Please, insert a valid column name for 1st input: ")
            
        if a in dataset.columns[0:3]:
            plt.plot(dataset.index, dataset[a])
            plt.xlabel("years")
            plt.ylabel(a)
            return plt.show()
        else:
            print("\n \n")
            print("To perform plotting you must choice columns [0-3]")
            print("\n")
            return dataset[a]
        
    else:
        if a not in dataset.columns:
            a=input("Please, insert a valid column name for the 1st input: ")
        if b not in dataset.columns:
            b=input("Please, insert a valid column name for the 2nd input: ")
        
        if a in dataset.columns[0:3] and b in dataset.columns[0:3]:
            plt.plot(dataset.index, dataset[a], dataset.index, dataset[b])
            plt.xlabel("years")
            plt.ylabel("Blue: 1st input. Orange: 2nd input")
            return plt.show()
        
        else:
            print("\n \n")
            print("To perform multiple plotting you must choice columns [0-3]")
            print("\n")