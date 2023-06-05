"""
Created on Thu Jan 26 14:11:08 2023

@author: Gaurav
"""
#%%
from IPython import display
import matplotlib.pyplot as plt

#%%
def parameter_plot_function_clusterwise(paper_metrics,display_technology,cluster_boundry,clustered_data,cluster_id):
    parameter=paper_metrics.columns.values.tolist()
    parameter.pop(0)
    #print(parameter)
    u=['Regional equality index']
    parameters=u+parameter
    
    for j in display_technology:
        fig = plt.figure()
        print('Techology: '+str(j)) 
        k=cluster_id-1
        print('cluster ID: '+ str(k+1))
        print()
        p=[]
        q=[]
        r=[]
        m=clustered_data[j][k+1]['SPORES'].index(clustered_data[j][k+1]['rep_sol'])
        img_dis=clustered_data[j][k+1]['rep_sol']
        display.Image("{}.jpg".format(img_dis))
        
        fig = plt.figure()
        ax = plt.subplot(111)
        for i in parameters:
            print('Parameter: '+ str(i))
            u=round(min(clustered_data[j][k+1][i]),2)
            v=round(max(clustered_data[j][k+1][i]),2)
            w=round(clustered_data[j][k+1][i][m],2)
            
            print('Value for representative SPORE: '+ str(w))
            print('Minimum value for the cluster: '+str(u))
            print('Maximum value for the cluster: '+str(v))
            print()
            
            p.append(min(clustered_data[j][k+1][i]))
            q.append(clustered_data[j][k+1][i][m])
            r.append(max(clustered_data[j][k+1][i]))
        
        ax.scatter(parameters,p,marker='v', c='m',s=30,label ='minimum value')
        ax.scatter(parameters,r,marker='^',c='m',s=30,label ='maximum value')
        ax.scatter(parameters,q,c='c',s=50,label ='representative solution value')
        
        for l in range(0,len(p)):
            ax.axvline(x=parameters[l], ymin=p[l], ymax=r[l],linestyle='dashed',linewidth=0.8,c='tab:gray')
            
        #plt.ylim(-0.1,1.1)
        plt.xticks(rotation=45)
        plt.ylabel('Paramter value')
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.show()        
        return (fig)
            
