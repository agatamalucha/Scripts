# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 20:06:33 2021

@author: agata
"""


import pandas as pd

dataset1=pd.read_csv("Top Girls Names 1964. Source CSO Ireland.csv")
dataset2=pd.read_csv("Top Girls Names 1979. Source CSO Ireland.csv")
dataset3=pd.read_csv("Top Girls Names 1997. Source CSO Ireland.csv")
dataset4=pd.read_csv("Top Girls Names 1988. Source CSO Ireland.csv")
dataset5=pd.read_csv("Top Girls Names 2006. Source CSO Ireland.csv")
dataset6=pd.read_csv("Top Girls Names 2018. Source CSO Ireland.csv")

dataset_girl=pd.concat([dataset1, dataset2, dataset3, dataset4, dataset5, dataset6])
dataset_girl= dataset_girl.drop_duplicates(subset="Name")
dataset_girl= dataset_girl[['Name']]


dataset1=pd.read_csv("Top Boys Names 1964. Source CSO Ireland.csv")
dataset2=pd.read_csv("Top Boys Names 1979. Source CSO Ireland.csv")
dataset3=pd.read_csv("Top Boys Names 1997. Source CSO Ireland.csv")
dataset4=pd.read_csv("Top Boys Names 1988. Source CSO Ireland.csv")
dataset5=pd.read_csv("Top Boys Names 2006. Source CSO Ireland.csv")
dataset6=pd.read_csv("Top Boys Names 2018. Source CSO Ireland.csv")

dataset_boy=pd.concat([dataset1, dataset2, dataset3, dataset4, dataset5, dataset6])
dataset_boy= dataset_boy.drop_duplicates(subset="Name")
dataset_boy= dataset_boy[['Name']]

names_all=pd.concat([dataset_girl,dataset_boy])
names_all.to_csv("names_all.csv")