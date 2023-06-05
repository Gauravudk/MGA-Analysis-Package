"""
Created on Thu Jan 26 14:11:08 2023

@author: Gaurav
"""

# In[ ]:

import pandas as pd
from statistics import mean
import collections
import warnings
from sklearn import preprocessing
warnings.filterwarnings('ignore')


from python_function.jenks_breaks_function import get_jenks_breaks
    
# In[ ]:


def clustered_data_function(ins_cap,gini_ins,paper_metrics,display_technology,cluster_number):
    
    cluster_boundry=pd.DataFrame()
    technology=ins_cap.columns.values.tolist()
    spore=technology[0]
    technology.pop(0)
    
    parameter=paper_metrics.columns.values.tolist()
    parameter.pop(0)
    
    #creates a dataframe with normalize value of installed capacity used while finding representative solution.
    norm_cap=pd.DataFrame(columns=technology)
    min_max_scaler = preprocessing.MinMaxScaler()
    for j in technology:
        x_scaled = min_max_scaler.fit_transform(ins_cap[[spore,j]])
        norm_cap.loc[:,j] = x_scaled[:,1]
    
    #application of clustering function
    for i in technology:
        tech=ins_cap[i].tolist() 
        breaks = get_jenks_breaks(tech, cluster_number)
        cluster_boundry[i]=breaks
    
    # storing of clustered data in the clustered data dictionary.
    clustered_data={}
    for j in technology:
        clustered_data[j]={}
        for k in range (0, len(cluster_boundry)-1):
            value_1=[]
            index_1=[]
            norm_1=[]
            ginic_1=[]
            mul_list_dict = collections.defaultdict(list)
            
            for i in range(0, len(ins_cap.SPORES)):
                if cluster_boundry[j][k]<=ins_cap[j].values[i]<cluster_boundry[j][k+1]:
                    value_1.append(ins_cap[j].values[i])
                    index_1.append(ins_cap[j].index[i])
                    norm_1.append(norm_cap[j].values[i])
                    ginic_1.append(gini_ins[j].values[i])
                    
                    for l in parameter:
                        mul_list_dict[l].append(paper_metrics[l].values[i])
                
            clustered_data[j][k+1]={}
            clustered_data[j][k+1]['installed_capacity']=value_1
            clustered_data[j][k+1]['SPORES']=index_1
            clustered_data[j][k+1]['normalized_capacity']=norm_1
            clustered_data[j][k+1]['Regional equality index']=ginic_1 

            for l in parameter:
                g=mul_list_dict[l]
                clustered_data[j][k+1][l]=g
    
#%% This block of code finds mean solution for each cluster.

    for j in technology:
        for k in range (0, len(cluster_boundry)-1):
            mul_list_dict = collections.defaultdict(list)
        
            mean_sol=[]
       
            for i in clustered_data[j][k+1]['SPORES']:
                for l in technology:
                    mul_list_dict[l].append(norm_cap[l].values[i])
               
                
            for l in technology:
                g=mul_list_dict[l]
                mean_sol.append(mean(g))

            clustered_data[j][k+1]['mean_sol']=mean_sol

#%%This block of code compares mean solution with all solutions to find representative soultion
#Then stores into clustered data dictionary.        
    for j in technology:
        for k in range (0, len(cluster_boundry)-1):
            abs_val_list=[]
            for i in clustered_data[j][k+1]['SPORES']:
                abs_val=0
                count=0
                for l in technology:
                    temp_list=[]
                    for n in range(len(clustered_data[j][k+1]['mean_sol'])):
                        temp_list.append(abs(clustered_data[j][k+1]['mean_sol'][n]-norm_cap[l].values[i]))
              
                    abs_val=abs_val+temp_list[count]
                    count=count+1
        
                abs_val_list.append(abs_val)
      
            x=pd.Series(abs_val_list).idxmin()
            clustered_data[j][k+1]['rep_sol']=clustered_data[j][k+1]['SPORES'][x]
    
    return(clustered_data,cluster_boundry)

