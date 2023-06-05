#!/usr/bin/env python
# coding: utf-8

#%% This block of code imports the libraries.


import pandas as pd
import warnings

warnings.filterwarnings('ignore')

#%% In this block we import the csv file.

#This particular file has the installed capacity of each technology at different
#location. The demo file is provided in the main folder for reference.

#Replace the current file with your csv file in the main folder and rename it 
#as installed_capacity_loc

data_1='installed_capacity_loc.csv'
cost=pd.read_csv(data_1)

#%% This block of code creates a dataframe with column names as technologies 
#present in the csv file.

techs=set(cost[cost.columns[1]])

gini_cost=pd.DataFrame(columns=techs)



#%% This block of code finds the regional equality index and store in the 
#dataframe created in the 2 block. 

for j in techs:
    
     
    df=cost[(cost[cost.columns[1]]==j)]
    #creates a dataframe with specific technology
    
    for k in range(len(set(cost[cost.columns[0]]))):
        df1=df[df[cost.columns[0]]==k]
        #creates a dataframe with specific technology and specific spore
        
        x=df1[cost.columns[5]].values.tolist()
        #Extracts installed capactiy for specific technology and specific spore
        
        numm=0
        #Formula of regional equality index
        for i in range(len(x)):
            for l in range(len(x)):
                temp=abs(x[l]-x[i])
                numm=numm+temp
        
        lenx=len(set(cost['locs']))
        meanx=sum(x)/lenx
        den=2*meanx*lenx*lenx
        
        if den==0:
            gini=0
        else:
            gini=numm/den
        
        reg_eq=1-gini
        
        
        gini_cost.loc[k,j] = reg_eq
        #stores the regional equality index in the dataframe

#%% This block of code converts dataframe into csv file

gini_cost.to_csv('gini.csv')

#%% Done 



