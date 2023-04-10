import pandas as pd
import numpy as np


def getDataFrame(infilename):
    df=pd.read_csv(infilename)
    return df


def parse_csv_file_to_dataframe(infilename, filetype='income/demographics', fileyear='year'):
    infile = open(infilename)
    #print(infilename)
    #Part of function to clean up Income Datasets
    if filetype=='income':
        line = infile.readline()
        #print(line)
        vals = line.split('\"')
        #print(vals)
        state = []
        incomes = []
        for line in infile:
            #print(line)
            vals = line.split(',')
            nvals = len(vals)
            #print(nvals)
            if nvals==14 and fileyear=='2000':
                if vals[0].find('Total population')<0 and vals[0].find('Number')<0 and vals[0].find('Percent')<0:
                    state.append(vals[0])
                    #print(state)
                    #print(vals)     
            else:
                newvals = line.split('\"')
                #print(newvals)
                if newvals[0].find('Number')<0:
                    continue
                # Pack the values
                icount = 0
                inc = []
                for i in range(1,len(newvals)):
                    x = newvals[i]
                    if len(x)>1:
                        x = int(x.replace(',',''))
                        inc.append(x)
                incomes.append(inc)
        incomes = np.array(incomes).T
        #print(incomes)
        d = {}
        d['State'] = state
        d['# of households'] = incomes[0]
        d['0-10000'] = incomes[1]
        d['10000-15000'] = incomes[2]
        d['15000-25000'] = incomes[3]
        d['25000-35000'] = incomes[4]
        d['35000-50000'] = incomes[5]
        d['50000-75000'] = incomes[6]
        d['75000-100000'] = incomes[7]
        d['100000-150000'] = incomes[8]
        d['150000-200000'] = incomes[9]
        d['200000-100000000'] = incomes[10]
        d['Median'] = incomes[11]
        d['Mean'] = incomes[12]
        df = pd.DataFrame.from_dict(d)

    #Part of function to clean up Population and Demographics Datasets
    elif filetype=='demographics':
        line = infile.readline()
        #print(line)
        vals = line.split('\"')
        #print(vals)
        state = []
        incomes = []
        for line in infile:
            #print(line)
            vals = line.split(',')
            nvals = len(vals)
            #print(nvals)
            if nvals==26:
                if vals[0].find('Total')<0 and vals[0].find('Percent')<0:
                    state.append(vals[0])
                    #print(vals)
            elif nvals==20:
                if vals[0].find('Total population')<0 and vals[0].find('Number')<0 and vals[0].find('Percent')<0:
                    state.append(vals[0])
                    #print(vals)
            else:
                newvals = line.split('\"')
                #print(newvals)
                if newvals[0].find('Estimate')<0 or newvals[0].find('Percent')>=0:
                    continue
                    
                #print('here')
                #print(newvals)
                #print(len(newvals))
                # Pack the values
                icount = 0
                inc = []
                for i in range(1,len(newvals)):
                    x = newvals[i]
                    #print(x)
                    #print(len(x))
                    if len(x)>1:
                        #print(x)
                        if x.find('.')>=0:
                            #print(x)
                            x = float(x.replace(',',''))
                        else:
                            x = int(x.replace(',',''))
                        inc.append(x)
                incomes.append(inc)
        #print(incomes)
        #for i in incomes:
            #print(len(i))
        incomes = np.array(incomes).T
        #print()
            #for i in incomes:
            #print(len(i))
            #print(i)
        d = {}
        d['State'] = state
        d['Population'] = incomes[0]
        d['Male'] = incomes[1]
        d['Female'] = incomes[2]
        d['Under 5 yrs'] = incomes[3]
        d['5-9 yrs'] = incomes[4]
        d['10-14 yrs'] = incomes[5]
        d['15-19 yrs'] = incomes[6]
        d['20-24 yrs'] = incomes[7]
        d['25-34 yrs'] = incomes[8]
        d['35-44 yrs'] = incomes[9]
        d['45-54 yrs'] = incomes[10]
        d['55-59 yrs'] = incomes[11]
        d['60-64 yrs'] = incomes[12]
        d['65-74 yrs'] = incomes[13]
        d['75-84 yrs'] = incomes[14]
        d['85 yrs and Older'] = incomes[15]
        d['Median Age'] = incomes[16]
        d['18 yrs and Older'] = incomes[17]
        d['65 yrs and Older'] = incomes[18]
        if fileyear=='2010' or fileyear=='2020':
            d['White'] = incomes[19]
            d['Black or African American'] = incomes[20]
            d['American Indian and Alaska Native'] = incomes[21]
            d['Asian'] = incomes[22]
            d['Native Hawaiian and Other Pacific Islander'] = incomes[23]
            d['Some Other Race'] = incomes[24]
        #print(d)
        #print(d['State'])
        df = pd.DataFrame.from_dict(d)
    return df

