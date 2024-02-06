import os
import re

# # Define the path to the directory containing the files
# path = "/media/kaiarmstrong/HDD2T/SPORTS_DATA/biomechanics_output/p01"

# # Define the list of files to be processed
# files = os.listdir(path)

# Function to process multiple directories and add matching files to a dictionary
def process_directories(directories, lookup_table):
    # Initialize an empty dictionary to store the filenames for each string in the lookup table
    matching_files = {}

    # Loop through the directories
    for directory in directories:
        # Get the list of files in the current directory
        files = os.listdir(directory)

        # Loop through the files in the current directory
        for file in files:
            # Check if any of the substrings in the lookup table are present in the filename
            for substring, string in lookup_table.items():
                if re.search(substring, file) and not re.search("SquatToBox", file) and not re.search("Squat_To_Box", file) and not re.search("squat_to_box", file) and not re.search("squattobox", file):
                    # If a match is found, add the filename to the matching_files dictionary
                    if directory not in matching_files:
                        matching_files[directory] = {}
                    if string not in matching_files[directory]:
                        matching_files[directory][string] = []
                    matching_files[directory][string].append(file)

            # Special case for "SquatToBox"
            if re.search("SquatToBox", file):
                if directory not in matching_files:
                    matching_files[directory] = {}
                if "SquatToBox" not in matching_files[directory]:
                    matching_files[directory]["SquatToBox"] = []
                matching_files[directory]["SquatToBox"].append(file)
            elif re.search("Squat_To_Box", file):
                if directory not in matching_files:
                    matching_files[directory] = {}
                if "SquatToBox" not in matching_files[directory]:
                    matching_files[directory]["SquatToBox"] = []
                matching_files[directory]["SquatToBox"].append(file)
            elif re.search("squat_to_box", file):
                if directory not in matching_files:
                    matching_files[directory] = {}
                if "SquatToBox" not in matching_files[directory]:
                    matching_files[directory]["SquatToBox"] = []
                matching_files[directory]["SquatToBox"].append(file)
            elif re.search("squattobox", file):
                if directory not in matching_files:
                    matching_files[directory] = {}
                if "SquatToBox" not in matching_files[directory]:
                    matching_files[directory]["SquatToBox"] = []
                matching_files[directory]["SquatToBox"].append(file)

    return matching_files

directories = [
        "/media/kaiarmstrong/HDD2T/SPORTS_DATA/biomechanics_output/p01",
        "/media/kaiarmstrong/HDD2T/SPORTS_DATA/biomechanics_output/p02",
        "/media/kaiarmstrong/HDD2T/SPORTS_DATA/biomechanics_output/p03",
        "/media/kaiarmstrong/HDD2T/SPORTS_DATA/biomechanics_output/p04",
        "/media/kaiarmstrong/HDD2T/SPORTS_DATA/biomechanics_output/p05",
        "/media/kaiarmstrong/HDD2T/SPORTS_DATA/biomechanics_output/p06",
        "/media/kaiarmstrong/HDD2T/SPORTS_DATA/biomechanics_output/p07",
    ]

# Define the lookup table as a dictionary
lookup_table = {
    # Substring: String
    "Static": "Static",
    "static": "Static",
    "Squat": "Squat",
    "squat": "Squat",
    "SquatToBox": "SquatToBox",
    "squattobox": "SquatToBox",
    "squat_to_box": "SquatToBox",
    "Squat_To_Box": "SquatToBox",
    "SitToStand": "SitToStand",
    "SitToStnd": "SitToStand",
    "sit_to_stand": "SitToStand",
    "Sit_To_Stand": "SitToStand",
    "sittostand": "SitToStand",
    "Balance_Left": "LeftBalance",
    "left_balance": "LeftBalance",
    "leftbalance": "LeftBalance",
    "Left_Balance": "LeftBalance",
    "Right_Balance": "RightBalance",
    "Balance_Right": "RightBalance",
    "right_balance": "RightBalance",
    "rightbalance": "RightBalance",
    "rightlbalance": "RightBalance",
    "LeftLunges": "LeftLunges",
    "left_lunge": "LeftLunges",
    "Left_Lunge": "LeftLunges",
    "leftlunge": "LeftLunges",
    "Lunge_Left": "LeftLunges",
    "RightLunges": "RightLunges",
    "right_lunge": "RightLunges",
    "Right_Lunge": "RightLunges",
    "rightlunge": "RightLunges",
    "Lunge_Right": "RightLunges",
    "LeftForwardLunge": "LeftLunges",
    "RightForwardLunge": "RightLunges",
}

# Initialize an empty dictionary to store the filenames for each string in the lookup table
matching_files = {}

for directory in directories:
    # Get the list of files in the current directory
    files = os.listdir(directory)

    # Loop through the files in the current directory
    for file in files:
        # Check if any of the substrings in the lookup table are present in the filename
        for substring, string in lookup_table.items():
            if re.search(substring, file) and not re.search("SquatToBox", file) and not re.search("Squat_To_Box", file) and not re.search("squat_to_box", file) and not re.search("squattobox", file):
                # If a match is found, add the filename to the matching_files dictionary
                if string not in matching_files:
                    matching_files[string] = []
                matching_files[string].append(file)

        # Special case for "SquatToBox"
        if re.search("SquatToBox", file):
            if "SquatToBox" not in matching_files:
                matching_files["SquatToBox"] = []
            matching_files["SquatToBox"].append(file)
        elif re.search("Squat_To_Box", file):
            if "SquatToBox" not in matching_files:
                matching_files["SquatToBox"] = []
            matching_files["SquatToBox"].append(file)
        elif re.search("squat_to_box", file):
            if "SquatToBox" not in matching_files:
                matching_files["SquatToBox"] = []
            matching_files["SquatToBox"].append(file)
        elif re.search("squattobox", file):
            if "SquatToBox" not in matching_files:
                matching_files["SquatToBox"] = []
            matching_files["SquatToBox"].append(file)


# Print the matching files
#print(matching_files)

for i in matching_files:
    print(i)
    print(len(matching_files[i]))

matching_files_new = process_directories(directories, lookup_table)

# Print the results
for i in matching_files_new:
    print(i)
    for j in matching_files_new[i]:
        print(j)
        print(len(matching_files_new[i][j]))
import pandas as pd
import matplotlib.pyplot as plt

# Function to plot a histogram of the dictionary
def plot_histogram(matching_files):
    # Initialize the number of rows and columns for the subplots
    num_rows = len(matching_files) // 2
    num_cols = 2

    # Add an extra row if necessary
    if len(matching_files) % 2 != 0:
        num_rows += 1

    # Create a figure with subplots
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(11.69, 8.27))

    # Loop through the directories
    for i, directory in enumerate(matching_files):
        # Initialize an empty list to store the data for the histogram
        data = []

        # Loop through the actions in each directory
        for action in matching_files[directory]:
            # Get the number of files for the current action
            num_files = len(matching_files[directory][action])

            # Append the data to the list
            data.append((action, num_files))

        # Create a pandas DataFrame from the data
        df = pd.DataFrame(data, columns=["Action", "Number of Files"])

        # Plot the histogram
        axs[i // 2, i % 2].bar(df["Action"], df["Number of Files"])
        #axs[i // 2, i % 2].set_xlabel("Action")
        #axs[i // 2, i % 2].set_ylabel("Count")
        axs[i // 2, i % 2].set_title(f"{directory[-3:]}")

    # Adjust the spacing between subplots
        
    plt.tight_layout()
    plt.subplots_adjust(hspace=0.2, wspace=0.2)

    # Show the figure
    
    plt.show()

plot_histogram(matching_files_new)