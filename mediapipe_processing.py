import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import pandas as pd
import os
import iio
import sys
import cv2

model_path = '/media/kaiarmstrong/HDD2T/SPORTS_DATA/pose_landmarker_heavy.task'


import cv2
import mediapipe as mp

def process_video(video_path):
    # Initialize MediaPipe Pose
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()

    # Open video file
    cap = cv2.VideoCapture(video_path)
    full_keypoints = []
    while cap.isOpened():
        # Read a frame
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame with MediaPipe Pose
        results = pose.process(rgb_frame)
        keypoints = []
        if results.pose_landmarks:

            
            keypoints.append(results.pose_world_landmarks)
        full_keypoints.append(keypoints)
        pose.close()
    print(full_keypoints)

results_pose = process_video("P01_Balance_1-DSC(1).avi")


"""body_parts = [
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
    return reshaped_df

def main():
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script_name.py input_video.mp4")
        sys.exit(1)

    # Get the input video file name from the command line arguments
    input_video = sys.argv[1]

    # Call the video_to_pose function
    output_df = video_to_pose(input_video)

    # Modify the output file name
    output_file = input_video.replace('.avi', '_mediapipe.csv')

    # Save the output DataFrame to a CSV file
    output_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    main()
"""