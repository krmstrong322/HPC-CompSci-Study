import cv2
import mediapipe as mp
import numpy as np
import sys
import os
import pandas as pd
from tqdm import tqdm

import warnings
warnings.filterwarnings('ignore')

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

body_parts = [
    "nose",
    "inner_eye_l",
    "eye_l",
    "outer_eye_l",
    "inner_eye_r",
    "eye_r",
    "outer_eye_r",
    "ear_l",
    "ear_r",
    "mouth_l",
    "mouth_r",
    "shoulder_l",
    "shoulder_r",
    "elbow_l",
    "elbow_r",
    "wrist_l",
    "wrist_r",
    "pinky_l",
    "pinky_r",
    "index_finger_l",
    "index_finger_r",
    "thumb_l",
    "thumb_r",
    "hip_l",
    "hip_r",
    "knee_l",
    "knee_r",
    "ankle_l",
    "ankle_r",
    "heel_l",
    "heel_r",
    "foot_index_l",
    "foot_index_r",
]


pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)


#vid_str = "P01_Balance_1-DSC(1).avi"



def process_video(vid_input):
    cap = cv2.VideoCapture(vid_input)
    output_folder = os.path.join(os.getcwd(), 'output/')

    if cap.isOpened() == False:
        print("Error opening video stream or file")
        raise TypeError

    full_keypoints = []
    while cap.isOpened():
        ret, image = cap.read()
        if not ret:
            break
        results = pose.process(image)
        keypoints = []
        for data_point in results.pose_landmarks.landmark:
            keypoints.append({
                                'X': data_point.x,
                                'Y': data_point.y,
                                'Z': data_point.z,
                                })
        full_keypoints.append(keypoints)

    pose.close()
    cap.release()
    #print(full_keypoints)
    #print(results)
    #print(results.pose_landmarks)

    df = pd.DataFrame(full_keypoints, columns=body_parts)

    reshaped_data = {}

    # Iterate through the original DataFrame and reshape the data
    for col_name, col_data in df.items():
        body_part = col_name.split(' - ')[-1]  # Extract the body part name
        for row_idx, cell in enumerate(col_data):
            if row_idx not in reshaped_data:
                reshaped_data[row_idx] = {}
            reshaped_data[row_idx][f'{body_part}_x'] = cell['X']
            reshaped_data[row_idx][f'{body_part}_y'] = cell['Y']
            reshaped_data[row_idx][f'{body_part}_z'] = cell['Z']

    # Create a new DataFrame from the reshaped data
    reshaped_df = pd.DataFrame.from_dict(reshaped_data, orient='index')
    #reshaped_df.to_csv(f'{output_folder}{vid_input}_keypoints.csv', index=False)
    return reshaped_df

working_directory = 'p01/'

file_list = []   # define file_list to save all dxf files
for subdir, dirs, files in os.walk(working_directory):
    for file in files:
        if file.endswith('.avi'):
            file_list.append(file)
os.chdir(working_directory)

for i in tqdm(file_list):
    tmp = process_video(i)
    output_file = file.replace('.avi', '_mediapipe.csv')
    tmp.to_csv(output_file, index=False)

""" 
input_directory = "p01/"
output_directory = "mp_output/p01/"

for file in tqdm(os.listdir(input_directory)):
    if file.endswith('avi'):
        input_new = input_directory + file
        tmp = process_video(input_new)
        output_file = file.replace('.avi', '_mediapipe.csv')
        tmp.to_csv(output_file, index=False)
    # Save the output DataFrame to a CSV file
    

"""
"""
if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python script_name.py input_directory output_directory")
        sys.exit(1)

    # Get the input and output directories from the command line arguments
    #input_directory = sys.argv[1]
    #output_directory = sys.argv[2]
        
    input_directory = "p01/"
    output_directory = "mp_output/p01/"

    process_directory(input_directory, output_directory)
"""