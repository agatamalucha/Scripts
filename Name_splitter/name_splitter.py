# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 18:25:29 2021

@author: agata
"""

import pandas as pd
import numpy as np

dataset = pd.read_csv("booknames.csv")
dataset["name"] = dataset["name"].str.replace("O ", "O'")
dataset["name"] = dataset["name"].str.replace("Mc ", "Mc")    #Mc Carthy
dataset["name"] = dataset["name"].str.replace("Mac ", "Mac")  # MacCArthy
dataset["name"] = dataset["name"].str.replace("St ", "St")    #St Ledger 
dataset["name"] = dataset["name"].str.replace("De  ", "De")   # De Barra

dataset["name_list"] = dataset["name"].str.split(" ")


dataset["first_name"] = dataset["name"].str.split(" ").str[0]

#unique_names = list(dataset["first_name"].unique())
#unique_names = ['Anna', 'Kathy', 'John', 'Marta', 'Maria', 'Rosemary', 'Orla', 'Niamh', 'Marie', 'James']

unique_names =pd.read_csv("names_all.csv")
unique_names=list(unique_names['Name'].unique())

def first_name_check(lst):
    names_list = []
    for element in lst:
        if element in unique_names:
            names_list.append(element)
    return names_list        

def last_name_check(lst):
    names_list = []
    for element in lst:
        if element not in unique_names:
            names_list.append(element)
    return names_list  



dataset["first_names"] = dataset["name_list"].apply(lambda x: first_name_check(x))

dataset["first_names"] = dataset["first_names"].str.join(" ")
dataset["first_names"] = dataset["first_names"].str.replace("Mac'", "Mac ")


dataset["last_names"] = dataset["name_list"].apply(lambda x: last_name_check(x))

#dataset["last_names"] = dataset["last_names"].str.join("-")




