import pandas as pd
import numpy as np



# Grabbed this from here
# https://gist.github.com/rogerallen/1583593
    
us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
}
    


def getDataFrame(infilename):
    df=pd.read_csv(infilename)
    return df


def parse_csv_file_to_dataframe(infilename, filetype, fileyear):
    infile = open(infilename)
    #print(infilename)
    #Part of function to clean up Income Datasets
    if filetype=='income' and fileyear=='2000':
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
            if nvals==14:
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
    
    elif filetype=='income' and (fileyear=='2010' or fileyear=='2020'):
        line = infile.readline()
        #print(line)
        vals = line.split('\"')
        #print(vals)
        state = []
        incomes = []
        STORE_NEXT = False
        for line in infile:
            #print(line)
            vals = line.split(',')
            nvals = len(vals)
            #print(nvals)
            if nvals==14:
                if vals[0].find('ouseholds')<0 and vals[0].find('amilies')<0:
                    state.append(vals[0])
                    #print(state)
                    #print(vals)     
                elif vals[0].find('Households')>=0:
                    STORE_NEXT = True
            else:
                # If the previous found Households
                if STORE_NEXT == False:
                    continue
                    
                # Skip for next time
                STORE_NEXT = False
                
                newvals = line.split('\"')
                #print(newvals)
                #print(len(newvals))
                if newvals[0].find('Estimate')<0:
                    continue
                    
                # Pack the values
                icount = 0
                inc = []
                inc.append(int(newvals[1].replace(',','')))
                pcts = newvals[2].split(',')
                for i in range(len(pcts)):
                    x = pcts[i]
                    if len(x)>1:
                        x = float(x[:-1])
                        inc.append(x)
                inc.append(int(newvals[3].replace(',',''))) # Median 
                inc.append(int(newvals[5].replace(',',''))) # Mean

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
        
        h = df['# of households']
        
        names = df.columns
        for name in names:
            #print(name)
            if name.find('-')>=0:
                pct = df[name]/100.0
                n = pct * h
                df[name] = n

    #Part of function to clean up Population and Demographics Datasets
    elif filetype=='demographics':
        line = infile.readline()
        #print(line)
        vals = line.split('\"')
        #print(vals)
        state = []
        incomes = []

        WORD_TO_FIND = 'Estimate'
        if fileyear=='2000':
            WORD_TO_FIND = 'Number'
        elif fileyear=='2010' or fileyear=='2020':
            WORD_TO_FIND = 'Estimate'
                        
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
                if vals[0].find('Total population')<0 and vals[0].find(WORD_TO_FIND)<0 and vals[0].find('Percent')<0:
                    state.append(vals[0])
                    #print(vals)
            else:
                newvals = line.split('\"')
                #print(newvals)
                
                if newvals[0].find(WORD_TO_FIND)<0 or newvals[0].find('Percent')>=0:
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
        #print("HERE!!!!")
        #for i in incomes:
        #    print(len(i))
        #    print(i)
        
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
        
    # Convert state names to abbreviations
    abbrv = []
    nentries = len(df)
    for i in range(nentries):
        state = df.iloc[i]['State']
        
        a = state
        if state in us_state_to_abbrev.keys():
            a = us_state_to_abbrev[state]
        abbrv.append(a)
        
    df['State'] = abbrv
        
    return df
