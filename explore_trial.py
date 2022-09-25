# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 10:03:13 2022

@author: prefrontal-panda
"""
#We will base our analysis on this: https://towardsdatascience.com/mining-biomarkers-from-breath-2975740b2d24

#Changing working directory for this file
import os
cwd = os.getcwd() #getting current working directory
print("Current working directory: {0}".format(cwd))
os.chdir('/Users/Me/Desktop/Python_proj/Single-omics-in-Py') #Changing the directory
cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))

#import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.ensemble import RandomForestClassifier
from sklearn.manifold import TSNE

#load in the proteomics dataset
prot = pd.read_csv('proteomics_SCx.csv', header=0, index_col=[0,1])

#Checking column names
list(prot.columns)

#Cleaning the dataset
#Resetting the index
prot = prot.reset_index()
list(prot.columns)
#removing the '_RAT' from the second column
prot['PG.ProteinNames'] = prot['PG.ProteinNames'].str.replace(r'_RAT', '')
prot = prot.rename(columns={"PG.ProteinNames": "Protein"}) #Renaming the column
#removing the first column as we don't need it
prot = prot.drop(columns=['PG.ProteinAccessions'])
#setting the index of the dataframe as the proteins
prot = prot.set_index('Protein')
#renaming the columns as 'strain_number'
prot.columns = ['GAERS 1', 'GAERS 2', 'GAERS 3', 'GAERS 4', 'GAERS 5', 'GAERS 6', 'NEC 1', 'NEC 2', 'NEC 3', 'NEC 4', 'NEC 5', 'NEC 6']
#Checking the final data frame
print(prot)

#Plotting the distribution of the relative protein intensities


