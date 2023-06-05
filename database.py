#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 21:44:35 2022

@author: ilyasabdulrahman
"""

import pymysql


def get_headlines_from_database(website):
    '''
    This function retrieves the headlines for a specific website from the database.
    Returns: a list of headlines
    '''
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="Poiu7890!2023",
        database="testdb"
    )

    cursor = connection.cursor()

    select_query = '''
    SELECT headline
    FROM headlines1
    WHERE website = %s
    ORDER BY id DESC
    LIMIT 10
    '''
    
    cursor.execute(select_query, (website,))
    headlines = [row[0] for row in cursor.fetchall()]

    cursor.close()
    connection.close()

    return headlines

website = "CNBC_NEWS"
print(get_headlines_from_database(website))
print(len(get_headlines_from_database(website)))

# connection = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="Poiu7890!2023",
#     database="testdb"
#     )


# cursor = connection.cursor()

# # Create a table to store the data
create_table_query = '''
CREATE TABLE headlines1 (
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    website VARCHAR(255) NOT NULL,
    headline VARCHAR(255) NOT NULL
)
'''

# cursor.execute(create_table_query)
    
# # Commit the changes to the database
# connection.commit()

# # Close the cursor and connection
# cursor.close()
# connection.close()