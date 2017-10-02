import pandas as pd
import numpy as np
import os


def ecgframe(filename):

    # Created dataframe from .datfile
    with open(r'C:\Users\Sarah\Research_data\data\ecg_data\{}'.format(filename), 'r') as f:
        next(f)
        df = pd.DataFrame(line.rstrip().split() for line in f)
        # Assigned Column names
        df.columns = ['TimeStamp', 'ECGLLRA', 'ECGLARA', 'ECGRESP', 'ECGVxRL']
        # Cleaned DataFrame for relevant data columns
        df.drop(['TimeStamp','ECGLARA', 'ECGRESP', 'ECGVxRL'], axis=1, inplace=True)

    return df


def gsrframe(filename):
    # Created dataframe from .datfile
    with open(r'C:\Users\Sarah\Research_data\data\gsr_data\{}'.format(filename), 'r') as f:
        # next(f)
        df = pd.DataFrame(line.rstrip().split() for line in f)
        # Assigned Column names
        df.columns = ['TimeStamp', 'GSR_DATA']
        # Cleaned DataFrame for relevant data columns
        df.drop(['TimeStamp'], axis=1, inplace=True)

    return df


def fetch_ecg_folder(ecg_path):
    dataSet_ecg = {}
    for file in os.listdir(ecg_path):
        dataSet_ecg[file] = ecgframe(file)

    return dataSet_ecg


def fetch_gsr_folder(gsr_path):
    dataSet_gsr = {}
    for file in os.listdir(gsr_path):
        dataSet_gsr[file] = gsrframe(file)

    return dataSet_gsr


def main():
    try:
        fetch_ecg_folder(ecg_path)
        fetch_gsr_folder(gsr_path)
    except Exception as ex:
        print("Unknown exception " + str(ex))


ecg_path = r'C:\\Users\Sarah\Research_data\data\ecg_dat'
gsr_path = r'C:\\Users\Sarah\Research_data\data\gsr_data'

main()
