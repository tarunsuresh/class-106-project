import csv
import plotly.express as px
import pandas as pd
import numpy as np

def setup():
    datapath="Student Marks vs Days Present.csv"
    dataSource=getDataSource(datapath)
    findCorrelation(dataSource)

def getDataSource(datapath):
    marks=[]
    daysPresent=[]
    with open(datapath) as f:
        data=csv.DictReader(f)
        for row in data :
            print(row)
            marks.append(float(row["Marks In Percentage"]))
            daysPresent.append(float(row["Days Present"]))
    return{ "x":marks,"y":daysPresent}

def findCorrelation(data):
    correlation=np.corrcoef(data["x"],data["y"])
    print("correlation coeffecient is "+str(correlation[0,1]))

setup()