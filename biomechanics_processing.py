from functions import *
import pandas as pd
import numpy as np
import os
from tqdm import tqdm
from scipy.signal import butter, _savitzky_golay, filtfilt

def butterworth_filter(data, cutoff_freq=6, order=2, fs=30, btype='low', damping=0.25):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff_freq / nyquist
    b, a = butter(order, normal_cutoff, btype=btype, analog=False, output='ba', fs=fs)
    y = filtfilt(b, a, data, method="gust")
    return y

def joints_from_smpl(input):
    data = input
    joints = data[1]['joints3d']
    lists = {}
    for i in range(len(joints)):
        lists[i] = list(more_itertools.collapse(joints[i]))
    df = pd.DataFrame(lists)
    df.reset_index(drop=True, inplace=True)
    df_transposed = df.T
    df_transposed.rename(columns=rename_dict_OP, inplace=True)
    return df_transposed

def mediapipe_to_biomechanics(input_df):
    input_df = pd.read_csv(input_df)
    biomechanics_df = create_dataset_st(input_df)
    biomechanics_df['index'] = biomechanics_df.index
    biomechanics_df['index'] = biomechanics_df['index'] / 30
    for column in biomechanics_df.columns:
        if column != 'index':
            biomechanics_df[column] = butterworth_filter(biomechanics_df[column], cutoff_freq=6, order=2, fs=30, btype='low', damping=0.25)

    return biomechanics_df

def vibe_to_biomechanics(input_pkl):
    data = joblib.load(input_pkl)
    df = joints_from_smpl(data)
    biomechanics_df = create_dataset_st(df)
    biomechanics_df['index'] = biomechanics_df.index
    biomechanics_df['index'] = biomechanics_df['index'] / 30
    for column in biomechanics_df.columns:
        if column != 'index':
            biomechanics_df[column] = butterworth_filter(biomechanics_df[column], cutoff_freq=6, order=2, fs=30, btype='low', damping=0.25)

    return biomechanics_df


# reshaped_df = pd.read_csv("/media/kaiarmstrong/HDD2T/SPORTS_DATA/P01_Balance_1-DSC(1)_mediapipe.csv")
# biomechanics_df = mediapipe_to_biomechanics(reshaped_df)
# print(biomechanics_df)
# biomechanics_df = vibe_to_biomechanics("P01_Balance_1-DSC(1).pkl")
# print(biomechanics_df)

directories = [
    "/media/kaiarmstrong/HDD2T/SPORTS_DATA/p01",
    "/media/kaiarmstrong/HDD2T/SPORTS_DATA/p02",
    "/media/kaiarmstrong/HDD2T/SPORTS_DATA/p03",
    "/media/kaiarmstrong/HDD2T/SPORTS_DATA/p04",
    "/media/kaiarmstrong/HDD2T/SPORTS_DATA/p05",
    "/media/kaiarmstrong/HDD2T/SPORTS_DATA/p06",
    "/media/kaiarmstrong/HDD2T/SPORTS_DATA/p07",
]

# Iterate over directories
for directory in directories:
    out_directory = os.path.join("/media/kaiarmstrong/HDD2T/SPORTS_DATA/biomechanics_output", os.path.basename(directory))

    # Create the output directory if it doesn't exist
    if not os.path.exists(out_directory):
        os.makedirs(out_directory)

    for file in tqdm(os.listdir(directory)):
        file_path = os.path.join(directory, file)

        try:
            if file.endswith("_mediapipe.csv"):
                biomechanics_df = mediapipe_to_biomechanics(file_path)
                out_filename = file.replace("mediapipe.csv", "biomechanics_mp.csv")
                out_path = os.path.join(out_directory, out_filename)
                biomechanics_df.to_csv(out_path, index=False)
            elif file.endswith(".pkl"):
                biomechanics_df = vibe_to_biomechanics(file_path)
                out_filename = file.replace(".pkl", "biomechanics_vibe.csv")
                out_path = os.path.join(out_directory, out_filename)
                biomechanics_df.to_csv(out_path, index=False)

        except KeyError as e:
            print(f"Error processing file {file}: {e}")
            continue