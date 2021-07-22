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

#################################### Function File For Anamoly Detection/Prepare ####################

def prep_logs(df):
    '''
    This function is designed to prep our curriculum logs for anomaly exploration

    It will convert things to datetime format
    and remove null values because it is a small percentage of our dataframe
    '''
    df.date = pd.to_datetime(df.date)

    df = df.dropna()

    return df


