import pandas as pd

def getDataFrame(infilename):
    df=pd.read_csv(infilename)
    return df