import itertools
import warnings
warnings.filterwarnings("ignore")

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import numpy as np
import pandas as pd
import math
from sklearn import metrics
from random import randint
from matplotlib import style
import seaborn as sns

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import MinMaxScaler

#################################### Function File For Anamoly Detection/Acquire ####################


sql_query ='SELECT * FROM cohorts'

# Create helper function to get the necessary connection url.
def get_connection(db_name):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    from env import host, user, password
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'


def get_data_from_sql(db_name, query ):
    """
    This function takes in a string for the name of the database that I want to connect to
    and a query to obtain my data from the Codeup server and return a DataFrame.
    db_name : df name in a string type
    query: aalready created query that was named as query 
    Example:
    query = '''
    SELECT * 
    FROM table_name;
    '''
    df = get_data_from_sql('zillow', query)
    """
    df = pd.read_sql(query, get_connection(db_name))
    return df


def acquire_logs():
    '''
    getting the dataframe from csv using seperators and the column specified form the list
    '''

    colnames = ['date', 'time', 'page', 'user_id', 'cohort_id', 'source_ip']
    df = pd.read_csv("anonymized-curriculum-access-07-2021.txt", 
                    sep="\s", 
                    header=None, 
                    names = colnames, 
                    usecols=[0, 1, 2, 3, 4, 5])
    return df


def df_summary(df):
    '''
    Function that complete the intial phases of the acquire phase of the pipeline

    datatypes of columns 
    dataframe shape 
    and some value counts
    '''
    print('The shape of our dataframe:\n')
    print(df.shape) ## <-- looking at our dataframe shape
    print('----------------------------------\n')

    print('Looking at our dataframe column and datatypes:\n')
    print(df.info()) ## looking at our df columns and datatypes
    print('----------------------------------\n')

    for col in df.columns:  ## <-- using list comprehension to look at our column value counts
        print(f'Value Counts For {col} Column:\n')
        print(df[col].value_counts())
        print('-------------------------------\n')


def acquire():
    #aquire first data frame
    colnames = ['date', 'endpoint', 'user_id', 'cohort_id', 'source_ip']
    df1 = pd.read_csv("anonymized-curriculum-access-07-2021.txt", 
                 sep="\s", 
                 header=None, 
                 names = colnames, 
                 usecols=[0, 2, 3, 4, 5])
    
    #acquire second df
    df2 = get_data_from_sql('curriculum_logs', sql_query)
    #drop columns that we don't need
    df2 = df2.drop(columns =[ 'deleted_at', 'slack'])
    
    #merge
    df = df1.merge(df2, left_on='cohort_id', right_on= 'id', how = 'left')
    
    # drop id because it is duplicated
    df.drop(columns= ['id'],inplace = True)
    
    return df