# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 04:42:54 2017

@author: Minkush
"""
import pandas as pd

def check(num):

	#importing data_sets
	if num == 0:
		data_set = pd.read_csv(r'C:\Users\Gaurav\Desktop\web-d\projects\hackathons\hackdtu\venv\backend\mk_blockchain\names.csv')
		test_set = pd.read_csv(r'C:\Users\Gaurav\Desktop\web-d\projects\hackathons\hackdtu\venv\backend\mk_blockchain\Final_db.csv')
	else:
		data_set = pd.read_csv(r'C:\Users\Gaurav\Desktop\web-d\projects\hackathons\hackdtu\venv\backend\mk_blockchain\Final_db.csv')
		test_set = pd.read_csv(r'C:\Users\Gaurav\Desktop\web-d\projects\hackathons\hackdtu\venv\backend\mk_blockchain\Final_db.csv')
	#training data_sets
	transactions = []
	for i in range(0,73):
	    transactions.append([str(data_set.values[i,j]) for j in range(0,3)])
	    
	from apyori import apriori
	rules = apriori(transactions,min_support = 0.0001,min_confidence = 0.002,min_lift = 1.2,min_length = 2)
	results_train = list(rules)

	#checking on real data
	transactions1 = []
	for i in range(0,50):
	    transactions1.append([str(test_set.values[i,j]) for j in range(0,3)])
	        
	rules1 = apriori(transactions1,min_support = 0.0001,min_confidence = 0.002,min_lift = 1.2,min_length = 2)
	results_test = list(rules1)
	count = 0

	#Finding the learning
	for f,b in zip(result_test,result_train):
	    if(f != b):
	        count+=1
	    if count > 2:
	        return 0
	return 1
