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

#################################### Function File For Anamoly Detection/Exploration ####################


def prep(df, user):
    df = df[df.user_id == user]
    df.date = pd.to_datetime(df.date)
    df = df.set_index(df.date)
    pages = df['page'].resample('d').count()
    return pages

def compute_pct_b(pages, span, weight, user):
    midband = pages.ewm(span=span).mean()
    stdev = pages.ewm(span=span).std()
    ub = midband + stdev*weight
    lb = midband - stdev*weight
    bb = pd.concat([ub, lb], axis=1)
    my_df = pd.concat([pages, midband, bb], axis=1)
    my_df.columns = ['pages', 'midband', 'ub', 'lb']
    my_df['pct_b'] = (my_df['pages'] - my_df['lb'])/(my_df['ub'] - my_df['lb'])
    my_df['user_id'] = user
    return my_df

def plt_bands(my_df, user):
    fig, ax = plt.subplots(figsize=(12,8))
    ax.plot(my_df.index, my_df.pages, label='Number of Pages, User: '+str(user))
    ax.plot(my_df.index, my_df.midband, label = 'EMA/midband')
    ax.plot(my_df.index, my_df.ub, label = 'Upper Band')
    ax.plot(my_df.index, my_df.lb, label = 'Lower Band')
    ax.legend(loc='best')
    ax.set_ylabel('Number of Pages')
    plt.show()

def find_anomalies(df, user, span, weight):
    pages = prep(df, user)
    my_df = compute_pct_b(pages, span, weight, user)
    # plt_bands(my_df, user)
    return my_df[my_df.pct_b>1]


def outlier_calculation(df, variable):
    '''
    calcualtes the lower and upper bound to locate outliers in variables
    '''
    quartile1, quartile3 = np.percentile(df[variable], [25,75])
    IQR_value = quartile3 - quartile1
    lower = quartile1 - (1.5 * IQR_value)
    upper = quartile3 + (1.5 * IQR_value)
    '''
    returns the lowerbound and upperbound values
    '''
    print(f'For {variable} the lower bound is {lower} and  upper bound is {upper}')
    df = df[(df[variable] > lower) & (df[variable] < upper)]
    return df

def report_unique_val (df):
    '''
    takes in a df and gives you a report of number of unique values and count values <15 (categorical)
    count values <15 (numerical)
    '''
    num_cols = df.select_dtypes(exclude = 'O').columns.to_list()
    cat_cols = df.select_dtypes(include = 'O').columns.to_list()
    for col in df.columns:
            print(f'**{col}**')
            le = df[col].nunique()
            print ('Unique Values : ', df[col].nunique())
            print(' ')
            if col in cat_cols and le < 15:
                print(df[col].value_counts())
            if col in num_cols and  le < 23:
                 print(df[col].value_counts().sort_index(ascending=True)) 
            elif col in num_cols and le <150:
                print(df[col].value_counts(bins=10, sort=False).sort_index(ascending=True))
            elif col in num_cols and le <1001:
                print(df[col].value_counts(bins=100, sort=False).sort_index(ascending=True))

            print('=====================================================')