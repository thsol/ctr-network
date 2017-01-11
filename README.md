# ctr-network
Code for processing data to create network on Gephi and matplotlib graphs 

This file explains the fields in the datasets of each .txt file in this folder



data_1.txt (100,000 records, 15.6 MB) - original dataset shortened to fewer records


⋅	id: ad identifier
⋅	click: 0/1 for non-click/click
⋅	hour: format is YYMMDDHH, so 14091123 means 23:00 on Sept. 11, 2014 UTC.
⋅	C1 -- anonymized categorical variable
⋅	banner_pos
⋅	site_id
⋅	site_domain
⋅	site_category
⋅	app_id
⋅	app_domain
⋅	app_category
⋅	device_id
⋅	device_ip
⋅	device_model
⋅	device_type
⋅	device_conn_type
⋅	C14-C21 -- anonymized categorical variables


The two files outputted on INotebook (data_2.txt and data_3.txt for nodes and edges respectively) imported into Gephi. You can find the code that created these files in code.txt file.

result_1.txt (13,076 records, 213 KB)

⋅	device ID (8 bit or newly generated concat of 16 bits to import as source)


result_2.txt (13,076 records, 442 KB)

⋅	device ID (8 bit hash or newly generated concat of 16 bit hash to import as source)
⋅	domain ID (8 bit hash)


result_3.txt (13,430 records, 352 KB)

⋅	ID (device ID)
⋅	degree
⋅	betweenness centrality
⋅	weighted degree


code.py

Python code used to preprocess the dataset and show its network components on a log-log graph scale
