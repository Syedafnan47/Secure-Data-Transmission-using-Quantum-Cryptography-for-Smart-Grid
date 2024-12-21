# Python program to demonstrate
# writing to CSV

import csv
#import imp
from rssivalue import rssimodel
import sys
 
# field names
#fields = ['Nodes','Node1_Shadow','Node1_Acoustic','Node2_Shadow','Node2_Acoustic','Node3_Shadow','Node3_Acoustic','Node4_Shadow','Node4_Acoustic']
fields = ['Nodes','Shadow_A1','Shadow_A2','Shadow_A3','Shadow_A4','Acoustic_A1','Acoustic_A2','Acoustic_A3','Acoustic_A4']
'''	
# data rows of csv file
my_module = imp.load_compiled("my_module","rssivalue.cpython-37.pyc")
rows=my_module.rssimodel()
''' 
rows=rssimodel(int(sys.argv[1])+1)	
# name of csv file
filename = "Rssi_values.csv"
	
# writing to csv file
with open(filename, 'w') as csvfile:
	# creating a csv writer object
	csvwriter = csv.writer(csvfile)
		
	# writing the fields
	csvwriter.writerow(fields)
		
	# writing the data rows
	csvwriter.writerows(rows)

#print("To do Localization of Nodes based on Rssi Value Run python3 localization.py")
