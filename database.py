#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 21:44:35 2022

@author: ilyasabdulrahman
"""

import pymysql
from app import nyt_list, fox_list, gau_list, cnbc_list, sky_list, ndtv_list, lsj_list, det_list


connection = pymysql.connect(
    host="localhost",
    user="root",
    password="Poiu7890!2023",
    database="testdb"
    )

print(connection)

cursor = connection.cursor()

# # Create a table to store the data
# create_table_query = '''
# CREATE TABLE SKY_NEWS_headlines (
# id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
# website VARCHAR(255) NOT NULL,
# headline VARCHAR(255) NOT NULL
# )
# '''

# cursor.execute(create_table_query)


# Iterate through the list of headlines from each website
for headline in nyt_list:
    # Insert data into the table
    insert_query = '''
    INSERT INTO NYTIMES_headlines (website, headline)
    VALUES (%s, %s)
    '''
    values = ('NY Times', headline)
    cursor.execute(insert_query, values)
    
for headline in fox_list:
    # Insert data into the table
    insert_query = '''
    INSERT INTO FOXNEWS_headlines (website, headline)
    VALUES (%s, %s)
    '''
    values = ('FOX NEWS', headline)
    cursor.execute(insert_query, values)

for headline in gau_list:
    # Insert data into the table
    insert_query = '''
    INSERT INTO THEGAURDIAN_headlines (website, headline)
    VALUES (%s, %s)
    '''
    values = ('THE GAURDIAN', headline)
    cursor.execute(insert_query, values)

for headline in cnbc_list:
    # Insert data into the table
    insert_query = '''
    INSERT INTO CNBC_NEWS_headlines (website, headline)
    VALUES (%s, %s)
    '''
    values = ('CNBC NEWS', headline)
    cursor.execute(insert_query, values)
    
for headline in ndtv_list:
    # Insert data into the table
    insert_query = '''
    INSERT INTO NDTV_NEWS_headlines (website, headline)
    VALUES (%s, %s)
    '''
    values = ('NDTV NEWS', headline)
    cursor.execute(insert_query, values)
    
for headline in lsj_list:
    # Insert data into the table
    insert_query = '''
    INSERT INTO LSJ_NEWS_headlines (website, headline)
    VALUES (%s, %s)
    '''
    values = ('LSJ NEWS', headline)
    cursor.execute(insert_query, values)

for headline in det_list:
    # Insert data into the table
    insert_query = '''
    INSERT INTO DET_NEWS_headlines (website, headline)
    VALUES (%s, %s)
    '''
    values = ('DETROIT NEWS', headline)
    cursor.execute(insert_query, values)
    
for headline in sky_list:
    # Insert data into the table
    insert_query = '''
    INSERT INTO SKY_NEWS_headlines (website, headline)
    VALUES (%s, %s)
    '''
    values = ('SKY NEWS', headline)
    cursor.execute(insert_query, values)
    

# Commit the changes to the database
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()