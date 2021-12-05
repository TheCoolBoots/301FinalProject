import os
import pandas as pd
import numpy as np

dataDirectory = 'CensusData'
outputDirectory = 'CleanCensusData'

fileNames = os.listdir(dataDirectory)

fileDict = {}

for fileName in fileNames:
    filepath = f'{dataDirectory}/{fileName}'
    with open(filepath, 'r') as file:
        fileFrame = pd.read_csv(filepath)
        fileDict[fileName] = fileFrame

for fileName, dataFrame in fileDict.items():
    dataFrame['census_block_group'] = dataFrame['census_block_group'].apply(lambda num: int(str(num)[:-7]))
    dataFrame.fillna(0, inplace=True)
    dataFrame = dataFrame.groupby('census_block_group').sum()

    dataFrame.to_csv(f'{outputDirectory}/{fileName}')