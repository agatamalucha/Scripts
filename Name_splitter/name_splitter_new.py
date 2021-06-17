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
dataset["last_name"] = dataset["name"].str.split(" ").str[-1]

#unique_names = list(dataset["first_name"].unique())
#unique_names = ['Anna', 'Kathy', 'John', 'Marta', 'Maria', 'Rosemary', 'Orla', 'Niamh', 'Marie', 'James']
dataset["items"]=dataset["name_list"].str.len()

unique_names =pd.read_csv("names_all.csv")
unique_names=list(unique_names['Name'].unique())


dataset_2 = dataset[dataset["items"] == 2]

dataset_4 = dataset[dataset["items"] == 4]
dataset_4["first_name"] = dataset_4["name"].str.split(" ").str[0:2].str.join(" ")
dataset_4["last_name"] = dataset_4["name"].str.split(" ").str[-2:].str.join("-")


dataset_3 = dataset[dataset["items"] == 3]


def first_name_check(lst):
    names_list = []
    for element in lst[1:2]:
        if element in unique_names:
            names_list.append(element)
        if len(element)== 1:
            new_element= element + "."
            names_list.append(new_element)
    return names_list        

def last_name_check(lst):
    names_list = []
    for element in lst[1:2]:
        if element not in unique_names and len(element) > 1:
            names_list.append(element)
    return names_list  



dataset_3["first_name2"] = dataset_3["name_list"].apply(lambda x: first_name_check(x))

dataset_3["first_name2"] = dataset_3["first_name2"].str.join(" ")

dataset_3["last_name0"] = dataset_3["name_list"].apply(lambda x: last_name_check(x))

dataset_3["last_name0"] = dataset_3["last_name0"].str.join(" ")
dataset_3["first_name"] = dataset_3["first_name"] + " " + dataset_3["first_name2"]

dataset_3["last_name"] = dataset_3["last_name0"]  + "-" + dataset_3["last_name"]






dataset_full = pd.concat([dataset_2, dataset_3, dataset_4])



dataset_full["last_name"] = dataset_full["last_name"].str.replace("-", " ")


dataset_full["last_name"] = dataset_full["last_name"].str.strip()


dataset_full["last_name"] = dataset_full["last_name"].str.replace(" ", "-")


dataset_full=dataset_full.drop(["last_name0","first_name2", "name_list","items" ],  axis=1)



















