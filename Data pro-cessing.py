import pandas as pd
import os
from matplotlib import pyplot
from numpy import where
import pandas as pd
import os
import json
import numpy as np
import pylab as plt
import time
import zipfile
import seaborn as sns
import random

from sklearn.neural_network import BernoulliRBM
from sklearn.tree import DecisionTreeClassifier

pd.options.mode.chained_assignment = None  # default='warn'
import warnings

from pandas.errors import SettingWithCopyWarning

warnings.simplefilter(action='ignore', category=(SettingWithCopyWarning))
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)


import pandas as pd


pd.options.mode.chained_assignment = None  # default='warn'
import warnings
import pandas as pd
from pandas.errors import SettingWithCopyWarning

warnings.simplefilter(action='ignore', category=(SettingWithCopyWarning))
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)


# List the json files in each folder'
path_1 = 'VeReMi_25200_28800_2022-9-12_2_59_13'
path_2 = 'VeReMi_28800_32400_2022-9-12_2_59_13'
path_3 = 'VeReMi_50400_54000_2022-9-11_19_11_27'
path_4 = 'VeReMi_54000_57600_2022-9-11_19_11_27'

list_of_files = []

for root, dirs, files in os.walk(path_1):
        for file in files:
           list_of_files.append(os.path.join(root, file))

for root, dirs, files in os.walk(path_2):
       for file in files:
          list_of_files.append(os.path.join(root, file))

for root, dirs, files in os.walk(path_3):
   for file in files:
       list_of_files.append(os.path.join(root, file))

for root, dirs, files in os.walk(path_4):
    for file in files:
        list_of_files.append(os.path.join(root, file))




# Each folder has one json file for the ground truth, we want to skip them
list_of_files.remove('VeReMi_25200_28800_2022-9-12_2_59_13\\traceGroundTruthJSON-7.json')
list_of_files.remove('VeReMi_28800_32400_2022-9-12_2_59_13\\traceGroundTruthJSON-8.json')
list_of_files.remove('VeReMi_50400_54000_2022-9-11_19_11_27\\traceGroundTruthJSON-14.json')
list_of_files.remove('VeReMi_54000_57600_2022-9-11_19_11_27\\traceGroundTruthJSON-15.json')

# Calculate the number of json
nb_each_json = []

for index in range(len(list_of_files)):
    nb_each_json.append(sum(1 for line in open(list_of_files[index])))

data = pd.DataFrame()
for index in range(len(list_of_files)):
    with open(list_of_files[index]) as f:
        # Read all the data in the files
        df = pd.DataFrame(json.loads(line) for line in f)
        # Read the following features from the name of json file (by splitting the file name)
        # labelRec: the label (0 normal, 13 (for this type of attack) attacker

        df['labelRec'] = list_of_files[index].rsplit('\\')[1].rsplit('-')[3].rsplit('A')[1]
        # receiver: the receiver ID
        df['receiver'] = list_of_files[index].rsplit('\\')[1].rsplit('-')[1]
        # moduleid: OMNeT++ module number, we don't need it now
        #df['moduleid'] = list_of_files[index].rsplit('\\')[1].rsplit('-')[4]
        data = pd.concat([data, df])
    print(index)

print(data.head())

# Choose the BSM where type = 3 (type = 2 GPS is just the sent messages, we will use the received messages, i.e. BSM)
print(data)
bsm = data
bsm = data[data.type == 3]

print(bsm)
# Pos, Spd, Acl, Hed, and their noise features have three axis: x,y,z.
# This function separates their x and y axis (z is always 0 for all, so we did not consider them.)
def clean_dataset(l, droped_features, data):
    for t in l:
        data[t + '_x'] = None
        data[t + '_y'] = None

    for j in l:
        data[j + '_x'] = data[j].apply(lambda row: row[0])
        data[j + '_y'] = data[j].apply(lambda row: row[1])
    data = data.drop(columns=l, axis=1)
    data.drop_duplicates(inplace=True)
    data.drop(columns=droped_features, inplace=True)
    return data

# The features who needs to be separated for the different axis
l = ['pos', 'pos_noise', 'spd', 'spd_noise', 'acl', 'acl_noise', 'hed', 'hed_noise']
# Using clean_dataset function, separate the features in l to their x and y axis
droped_features = []
bsm = clean_dataset(l, droped_features, bsm)
print(bsm)

bsm.dtypes
bsm['receiver'] = bsm['receiver'].astype("float64")
# bsm['sender'] = bsm['sender'].astype("float64")
bsm['labelRec'] = bsm['labelRec'].astype("int64")

bsm.head()
# Receiver - Sender matching

labelization = bsm[['receiver','labelRec']]
labelization.drop_duplicates(inplace=True)
bsm = bsm.drop(columns=['receiver','labelRec'], axis = 1)
bsm = pd.merge(bsm, labelization ,left_on='sender',right_on='receiver',how='left')
bsm.rename(columns={'labelRec':'label'},inplace=True)
bsm = bsm.drop(columns=['receiver'], axis = 1)
bsm = bsm.dropna()
# or:  bsm.dropna(inplace = True)
bsm.head()
bsm.describe()
bsm.columns
bsm.dtypes
bsm['label'] = bsm['label'].astype("int64")
# Number of lines in the dataset
len(bsm)
# Number of normal vehicles (0) and number of attackers (13) in the dataset
bsm.label.value_counts()
print(len(bsm))
# Storage of the data#bsm.to_csv('bsm.csv')
### Read the saved data
#bsm_copy = pd.read_csv('bsm.csv')
#bsm_copy.head()
bsm.to_csv('EventalStopFullPathes.csv')

exit(0)