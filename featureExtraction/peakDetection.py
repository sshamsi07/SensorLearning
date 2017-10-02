import numpy as np
import pandas as pd
import matplotlib as plt
import scipy as sci
from data import Framing


# from biosppy.signals import ecg


# Import data frame from Framing module in data package
def dataframe_to_array(dictionary, filename):
    # Converting data frame into array
    ecg_arr = dictionary[filename].values

    return ecg_arr


# Method to get R-peaks
def get_rpeaks(ecg_arr):
    rpeaks = ecg.ecg(signal=ecg_arr, sampling_rate=500., show=True)

    return rpeaks
