import pandas as pd
import numpy as np
import scipy.stats as stats
import os

# Function to calculate the area under the curve
def area_under_curve(x, y):
    return np.trapz(y, x)

# Function to calculate the area under the curve for each column in a dataframe
def calculate_area_under_curve(df):
    areas = {}
    for col in df.columns:
        areas[col] = area_under_curve(df.index, df[col])
    return areas

# Function to calculate the area under the curve for each column in multiple dataframes
def calculate_area_under_curve_multiple(dfs):
    areas_dict = {}
    for df in dfs:
        areas = calculate_area_under_curve(df)
        for col, area in areas.items():
            if col not in areas_dict:
                areas_dict[col] = []
            areas_dict[col].append(area)
    return areas_dict

#areas_dict = calculate_area_under_curve_multiple([df1, df2, df3])

def calculate_correlation(areas_dict):
    # Extract the lists of areas for columns 'A' and 'B'
    areas_A = areas_dict['A']
    areas_B = areas_dict['B']
    
    # Calculate the Pearson correlation coefficient
    corr, p_value = stats.pearsonr(areas_A, areas_B)
    
    return corr, p_value

#corr, p_value = calculate_correlation(areas_dict)

directories = [
    "/media/kaiarmstrong/HDD2T/SPORTS_DATA/p01",
    "/media/kaiarmstrong/HDD2T/SPORTS_DATA/p02",
    "/media/kaiarmstrong/HDD2T/SPORTS_DATA/p03",
    "/media/kaiarmstrong/HDD2T/SPORTS_DATA/p04",
    "/media/kaiarmstrong/HDD2T/SPORTS_DATA/p05",
    "/media/kaiarmstrong/HDD2T/SPORTS_DATA/p06",
    "/media/kaiarmstrong/HDD2T/SPORTS_DATA/p07",
]

squat = []
squat_to_box = []
sit_to_stand = []
left_balance = []
right_balance = []
left_lunges = []
right_lunges = []



for directory in directories:
    for file in os.listdir(directory):
        if "squat" in file:
            squat.append(directory + "/" + file)
        elif "squat_to_box" in file:
            squat_to_box.append(directory + "/" + file)
        elif "sit_to_stand" in file:
            sit_to_stand.append(directory + "/" + file)
        elif "left_balance" in file:
            left_balance.append(directory + "/" + file)
        elif "right_balance" in file:
            right_balance.append(directory + "/" + file)
        elif "left_lunges" in file:
            left_lunges.append(directory + "/" + file)
        elif "right_lunges" in file:
            right_lunges.append(directory + "/" + file)


