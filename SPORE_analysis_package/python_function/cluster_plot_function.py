"""
Created on Thu Jan 26 14:11:08 2023

@author: Gaurav
"""

#%%

import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from IPython import display

#%%


def cluster_plot_function(display_technology,cluster_boundry,clustered_data):
    #resolution_value = 1600

    col=['k', 'r', 'b', 'c', 'm', 'y']
    for j in display_technology:
        fig = plt.figure()
        print('Techology: '+str(j))
        for k in range (0, len(cluster_boundry)-1):
            m=clustered_data[j][k+1]['SPORES'].index(clustered_data[j][k+1]['rep_sol'])
            for l in range(len(clustered_data[j][k+1]['installed_capacity'])):
                plt.scatter(clustered_data[j][k+1]['SPORES'][l],clustered_data[j][k+1]['installed_capacity'][l],c=col[k],s=10, linewidth=0)

            plt.scatter(clustered_data[j][k+1]['SPORES'][m],clustered_data[j][k+1]['installed_capacity'][m],c='tab:gray',s=50, edgecolor='black', linewidth=1,label ='representative solution')
            plt.xlabel('SPORES')
            if display_technology =='biofuel_supply':
                plt.ylabel('Installed capacity in GW')
            else:
                plt.ylabel('Installed capacity in GW')
            plt.title(j)
            #plt.savefig(j,format="png", dpi=resolution_value)

            print('cluster ID: '+ str(k+1))
            print('Number of SPORES: ' +str(len(clustered_data[j][k+1]['SPORES'])))
            print('Id of representative SPORE: '+str(clustered_data[j][k+1]['rep_sol']))
            print('Installed capacity of representative SPORE: ' +str(clustered_data[j][k+1]['installed_capacity'][m])+'GW')
            print('Minimum install capacity in the cluster: ' + str(min(clustered_data[j][k+1]['installed_capacity']))+'GW')
            print('Maxmium install capacity in the cluster: '+ str(max(clustered_data[j][k+1]['installed_capacity']))+'GW' )
            print()
            display.Image("{}.jpg".format(m))
        plt.show()
        return (fig)
        print()
