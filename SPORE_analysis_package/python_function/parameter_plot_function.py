"""
Created on Thu Jan 26 14:11:08 2023

@author: Gaurav
"""

import matplotlib.pyplot as plt
import collections

#%%
def parameter_plot_function(paper_metrics,display_technology,cluster_boundry,clustered_data,cluster_number): 
    parameter=paper_metrics.columns.values.tolist()
    parameter.pop(0)
    #print(parameter)
    u=['Regional equality index']
    parameters=u+parameter
    cluster_list=list(range(1, cluster_number+1))
    
  
    
    for j in display_technology:
        fig = plt.figure()
        mul_list_dict = collections.defaultdict(list)
        print('Techology: '+str(j))
        print()
        
        for k in range (0, len(cluster_boundry)-1):
            m=clustered_data[j][k+1]['SPORES'].index(clustered_data[j][k+1]['rep_sol'])
       
            for l in parameters:
                mul_list_dict[l].append(clustered_data[j][k+1][l][m])
            
        fig = plt.figure()
        ax = plt.subplot(111)
        for l in parameters:
            c=mul_list_dict[l]
        
            ax.scatter(cluster_list,c)
            ax.plot(cluster_list,c,label=l)
        plt.xticks(cluster_list)
        plt.xlabel('Cluster_id')
        plt.ylabel('Parameter value')
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    
    plt.show() 
    return (fig)

