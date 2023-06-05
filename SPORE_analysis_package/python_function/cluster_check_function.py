"""
Created on Thu Jan 26 14:11:08 2023

@author: Gaurav
"""
#%%
import collections
from python_function.clustered_data_function import clustered_data_function
from statistics import mean

#%%
def cluster_check_function(ins_cap,gini_ins,paper_metrics,display_technology,cluster_number):
    [clusters,cluster_boundry]=clustered_data_function(ins_cap,gini_ins,paper_metrics,display_technology,cluster_number)
    parameter=paper_metrics.columns.values.tolist()
    parameter.pop(0)
    u=['Regional equality index']
    parameters=u+parameter
    cluster_list=list(range(1, cluster_number+1))
   
    for j in display_technology:
        mul_list_dict = collections.defaultdict(list)
        
        div_para=[]
        check_mat=[]
        for k in range (0, len(cluster_boundry)-1):
            m=clusters[j][k+1]['SPORES'].index(clusters[j][k+1]['rep_sol'])
       
            for l in parameters:
                mul_list_dict[l].append(clusters[j][k+1][l][m])
     
    # this block of code checks for number of cluster
        for n in parameters:
            
            
            col=[]
            for u in range(0,len(cluster_list)):
                for v in range(0,len(cluster_list)):
                    if u!=v:
                        col.append(abs(mul_list_dict[n][u]-mul_list_dict[n][v]))
                        
            div_para.append((min(col)))

    
        for s in range(len(div_para)):
            if div_para[s]<0.015: # check how much percent of data is within range of 1.5% of each other, if less than 1.5% added to list
                check_mat.append(1)
            else:
                check_mat.append(0)
    
        if mean(check_mat)>0.3333:
            return(cluster_number-1)
            break
        
       
    
       

