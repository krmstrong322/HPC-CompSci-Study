from functions import *
import pandas as pd
import numpy as np
import os
from tqdm import tqdm
from scipy.signal import butter, cheby1, savgol_filter, filtfilt, lfilter
import matplotlib.pyplot as plt

def savitzky_golay_filter(data, window_length=15, polyorder=3):
    y = savgol_filter(data, window_length=window_length, polyorder=polyorder)
    return y

def butterworth_filter(data, cutoff_freq=6, order=2, fs=30, btype='low', damping=0.25):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff_freq / nyquist
    b, a = butter(order, normal_cutoff, btype=btype, analog=False, output='ba', fs=fs)
    y = filtfilt(b, a, data, method="gust", irlen=100)
    return y


def plot_signals(time, original, filtered_butter, filtered_sg, title):
    plt.plot(time, original, label='Original')
    plt.plot(time, filtered_butter, label='Butterworth Filtered')
    plt.plot(time, filtered_sg, label='Savitzky-Golay Filtered')
    plt.title(title)
    plt.legend()


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
    #for column in input_df.columns:
    #    if column != 'index':
    #        input_df[column] = butterworth_filter(input_df[column], cutoff_freq=6, order=2, fs=30, btype='low', damping=0.25)
    biomechanics_df = create_dataset_st(input_df)
    biomechanics_df['index'] = biomechanics_df.index
    biomechanics_df['index'] = biomechanics_df['index'] / 30
    #for column in biomechanics_df.columns:
    #    if column != 'index':
    #        biomechanics_df[column] = butterworth_filter(biomechanics_df[column], cutoff_freq=6, order=2, fs=30, btype='low', damping=0.25)

    return biomechanics_df

def mediapipe_to_biomechanics_smoothbefore(input_df):
    input_df = pd.read_csv(input_df)
    for column in input_df.columns:
        if column != 'index':
            input_df[column] = butterworth_filter(input_df[column], cutoff_freq=6, order=2, fs=30, btype='low', damping=0.25)
    biomechanics_df = create_dataset_st(input_df)
    biomechanics_df['index'] = biomechanics_df.index
    biomechanics_df['index'] = biomechanics_df['index'] / 30
    #for column in biomechanics_df.columns:
    #    if column != 'index':
    #        biomechanics_df[column] = butterworth_filter(biomechanics_df[column], cutoff_freq=6, order=2, fs=30, btype='low', damping=0.25)

    return biomechanics_df

def mediapipe_to_biomechanics_smoothafter(input_df):
    input_df = pd.read_csv(input_df)
    #for column in input_df.columns:
    #    if column != 'index':
    #        input_df[column] = butterworth_filter(input_df[column], cutoff_freq=6, order=2, fs=30, btype='low', damping=0.25)
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

column_name = 'right_knee_flexion'

biomechanics_smoothafter = mediapipe_to_biomechanics_smoothafter("/media/kaiarmstrong/HDD2T/SPORTS_DATA/P01_Squat_1-DSC(1)_mediapipe.csv")
biomechanics_smoothbefore = mediapipe_to_biomechanics_smoothbefore("/media/kaiarmstrong/HDD2T/SPORTS_DATA/P01_Squat_1-DSC(1)_mediapipe.csv")

biomechanics_df = mediapipe_to_biomechanics("/media/kaiarmstrong/HDD2T/SPORTS_DATA/P01_Squat_1-DSC(1)_mediapipe.csv")

# smooth_1 = butterworth_filter(biomechanics_df[column_name], cutoff_freq=6, order=1, fs=30, btype='low', damping=0.25)
# smooth_2 = butterworth_filter(biomechanics_df[column_name], cutoff_freq=6, order=2, fs=30, btype='low', damping=0.25)
# smooth_3 = butterworth_filter(biomechanics_df[column_name], cutoff_freq=6, order=3, fs=30, btype='low', damping=0.25)
# smooth_4 = butterworth_filter(biomechanics_df[column_name], cutoff_freq=6, order=4, fs=30, btype='low', damping=0.25)
# smooth_5 = butterworth_filter(biomechanics_df[column_name], cutoff_freq=6, order=5, fs=30, btype='low', damping=0.25)
# smooth_6 = butterworth_filter(biomechanics_df[column_name], cutoff_freq=6, order=6, fs=30, btype='low', damping=0.25)
# smooth_7 = butterworth_filter(biomechanics_df[column_name], cutoff_freq=6, order=7, fs=30, btype='low', damping=0.25)

# plt.plot(biomechanics_df['index'], biomechanics_df[column_name], label='Original')
# plt.plot(biomechanics_df['index'], smooth_1, label='Order 1')
# plt.plot(biomechanics_df['index'], smooth_2, label='Order 2')
# plt.plot(biomechanics_df['index'], smooth_3, label='Order 3')
# plt.plot(biomechanics_df['index'], smooth_4, label='Order 4')
# plt.plot(biomechanics_df['index'], smooth_5, label='Order 5')
# plt.plot(biomechanics_df['index'], smooth_6, label='Order 6')
# plt.plot(biomechanics_df['index'], smooth_7, label='Order 7')
# plt.legend()
# plt.show()


# plt.plot(biomechanics_smoothafter['index'], biomechanics_smoothafter['right_knee_flexion'], label='Smooth After')
# plt.plot(biomechanics_smoothbefore['index'], biomechanics_smoothbefore['right_knee_flexion'], label='Smooth Before')
# plt.legend()
# plt.show()

# reshaped_df = pd.read_csv("/media/kaiarmstrong/HDD2T/SPORTS_DATA/P01_Balance_1-DSC(1)_mediapipe.csv")
# biomechanics_df = mediapipe_to_biomechanics(reshaped_df)
# print(biomechanics_df)
# biomechanics_df = vibe_to_biomechanics("P01_Balance_1-DSC(1).pkl")
# print(biomechanics_df)

biomechanics_df_f = mediapipe_to_biomechanics("/media/kaiarmstrong/HDD2T/SPORTS_DATA/P01_Squat_1-DSC(fused)_mediapipe.csv")
biomechanics_df_1 = mediapipe_to_biomechanics("/media/kaiarmstrong/HDD2T/SPORTS_DATA/P01_Squat_1-DSC(1)_mediapipe.csv")
biomechanics_df_2 = mediapipe_to_biomechanics("/media/kaiarmstrong/HDD2T/SPORTS_DATA/P01_Squat_1-DSC(2)_mediapipe.csv")

#plt.plot(biomechanics_df_f['index'], biomechanics_df_f['right_knee_flexion'], label='Fused')
#plt.plot(biomechanics_df_1['index'], biomechanics_df_1['right_knee_flexion'], label='1')
#plt.plot(biomechanics_df_2['index'], biomechanics_df_2['right_knee_flexion'], label='2')

#plt.show()
# Original vs Butterworth Filtered
filtered_butter = butterworth_filter(biomechanics_df[column_name], cutoff_freq=6, order=2, fs=30, btype='low', damping=0.25)

# Original vs Savitzky-Golay Filtered
filtered_sg = savitzky_golay_filter(biomechanics_df[column_name], window_length=15, polyorder=3)
plot_signals(biomechanics_df['index'], biomechanics_df[column_name], filtered_butter, filtered_sg, 'butter vs savgol')

plt.tight_layout()
plt.show()

#filtered_sg_f = savitzky_golay_filter(biomechanics_df_f[column_name], window_length=15, polyorder=3)
#filtered_sg_1 = savitzky_golay_filter(biomechanics_df_1[column_name], window_length=15, polyorder=3)
#filtered_sg_2 = savitzky_golay_filter(biomechanics_df_2[column_name], window_length=15, polyorder=3)


""" 
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
"""