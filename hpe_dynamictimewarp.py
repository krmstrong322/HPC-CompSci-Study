import pandas as pd
from fastdtw import fastdtw
from scipy.interpolate import RegularGridInterpolator
import numpy as np

def load_pose_sequence(file_path):
    # Load pose sequence from CSV file
    pose_df = pd.read_csv(file_path)
    print(pose_df.shape)
    # Exclude the first column and extract the rest
    pose_sequence = pose_df.iloc[:, 1:].values
    return pose_sequence

def get_columns_names(input):
    input_df = pd.read_csv(input)
    return input_df.iloc[:, 1:].columns

column_names = get_columns_names('/media/kaiarmstrong/HDD2T/SPORTS_DATA/P01_Squat_1-DSC(1)_mediapipe.csv')

def fuse_pose_sequences(sequence1, sequence2):
    # Use Dynamic Time Warping to align and fuse pose sequences
    _, path = fastdtw(sequence1, sequence2)
    
    # Create a new fused pose sequence
    fused_sequence = []
    for i, j in path:
        # Take the average of corresponding points from both sequences
        fused_point = (sequence1[i] + sequence2[j]) / 2
        fused_sequence.append(fused_point)

    return pd.DataFrame(np.array(fused_sequence), columns=column_names)

def save_fused_pose_sequence(fused_sequence, output_file):
    # Save the fused pose sequence to a new CSV file
    fused_sequence.to_csv(output_file, index=False)

if __name__ == "__main__":
    # Specify the paths to the two CSV files
    file1_path = '/media/kaiarmstrong/HDD2T/SPORTS_DATA/P01_Squat_1-DSC(1)_mediapipe.csv'
    file2_path = '/media/kaiarmstrong/HDD2T/SPORTS_DATA/P01_Squat_1-DSC(2)_mediapipe.csv'


    # Load pose sequences from CSV files?
    pose_sequence1 = load_pose_sequence(file1_path)
    pose_sequence2 = load_pose_sequence(file2_path)

    # Fuse the pose sequences using Dynamic Time Warping
    fused_sequence = fuse_pose_sequences(pose_sequence1[:-15], pose_sequence2)

    # Specify the path for the output CSV file
    output_file_path = '/media/kaiarmstrong/HDD2T/SPORTS_DATA/P01_Squat_1-DSC(fused)_mediapipe.csv'

    # Save the fused pose sequence to a new CSV file
    save_fused_pose_sequence(fused_sequence, output_file_path)
