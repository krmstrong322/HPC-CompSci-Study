#!/bin/bash

# Set the path to the directory containing video files
input_directory="/media/kaiarmstrong/HDD2T/SPORTS_DATA/p01"

# Set the path to the output folder
mkdir "/media/kaiarmstrong/HDD2T/SPORTS_DATA/vibe_output/p01"
output_folder="/media/kaiarmstrong/HDD2T/SPORTS_DATA/vibe_output/p01/"

# Set the tracking method, detector, and other options
tracking_method="bbox"
detector="maskrcnn"


# Activate Conda environment
source activate pytorch1.13_vibe

# Iterate over each video file in the input directory
for video_file in "$input_directory"/*.avi; do
    # Extract the file name without extension
    file_name=$(basename -- "$video_file")
    file_name_no_ext="${file_name%.*}"

    # Run the Python command for each video file
    python demo.py --vid_file "$video_file" --output_folder "${output_folder}${file_name_no_ext}/" --tracking_method "$tracking_method" --detector "$detector" --no_render
done

# Deactivate Conda environment
conda deactivate

