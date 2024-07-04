import re
import matplotlib.pyplot as plt
import pandas as pd
import time
from datetime import datetime

# Function to extract temperature value from the byte sequence
def extract_temperature(byte_sequence):
    bytes_list = byte_sequence.split()
    byte0 = int(bytes_list[0], 16)
    byte1 = int(bytes_list[1], 16)
    temperature_value = (byte0 * 256 + byte1) / 10 - 200
    return temperature_value

# Function to convert Unix timestamp to HH:MM:SS format
def convert_timestamp(unix_timestamp):
    return datetime.utcfromtimestamp(float(unix_timestamp)).strftime('%H:%M:%S')

# Initialize lists to store temperature values and timestamps
front_right_tire_data = []
front_left_tire_data = []
rear_left_tire_data = []
rear_right_tire_data = []

# Open the file and process each line
with open('extracted_messages.txt', 'r') as file:
    for line in file:
        match_front_right = re.search(r'Timestamp: (\d+\.\d+)\s+ID: (033[0-3])\s+S\s+DLC:\s+8\s+((?:[\dA-Fa-f]{2}\s+){8})', line)
        match_front_left = re.search(r'Timestamp: (\d+\.\d+)\s+ID: (031[0-3])\s+S\s+DLC:\s+8\s+((?:[\dA-Fa-f]{2}\s+){8})', line)
        match_rear_left = re.search(r'Timestamp: (\d+\.\d+)\s+ID: (035[0-3])\s+S\s+DLC:\s+8\s+((?:[\dA-Fa-f]{2}\s+){8})', line)
        match_rear_right = re.search(r'Timestamp: (\d+\.\d+)\s+ID: (037[0-1])\s+S\s+DLC:\s+8\s+((?:[\dA-Fa-f]{2}\s+){8})', line)
        if match_front_right:
            unix_timestamp = match_front_right.group(1)
            human_readable_timestamp = convert_timestamp(unix_timestamp)
            byte_sequence = match_front_right.group(3)
            temperature = extract_temperature(byte_sequence)
            front_right_tire_data.append((human_readable_timestamp, temperature))
        if match_front_left:
            unix_timestamp = match_front_left.group(1)
            human_readable_timestamp = convert_timestamp(unix_timestamp)
            byte_sequence = match_front_left.group(3)
            temperature = extract_temperature(byte_sequence)
            front_left_tire_data.append((human_readable_timestamp, temperature))
        if match_rear_left:
            unix_timestamp = match_rear_left.group(1)
            human_readable_timestamp = convert_timestamp(unix_timestamp)
            byte_sequence = match_rear_left.group(3)
            temperature = extract_temperature(byte_sequence)
            rear_left_tire_data.append((human_readable_timestamp, temperature))
        if match_rear_right:
            unix_timestamp = match_rear_right.group(1)
            human_readable_timestamp = convert_timestamp(unix_timestamp)
            byte_sequence = match_rear_right.group(3)
            temperature = extract_temperature(byte_sequence)
            rear_right_tire_data.append((human_readable_timestamp, temperature))

# Group the data into sets of 16
front_right_grouped_data = [front_right_tire_data[i:i + 16] for i in range(0, len(front_right_tire_data), 16)]
front_left_grouped_data = [front_left_tire_data[i:i + 16] for i in range(0, len(front_left_tire_data), 16)]
rear_left_grouped_data = [rear_left_tire_data[i:i + 16] for i in range(0, len(rear_left_tire_data), 16)]
rear_right_grouped_data = [rear_right_tire_data[i:i + 16] for i in range(0, len(rear_right_tire_data), 16)]

# Ensure the number of groups is the same for all tires
num_groups = max(len(front_right_grouped_data), len(front_left_grouped_data), len(rear_left_grouped_data), len(rear_right_grouped_data))

# Plot each group in a rectangle, with a delay between each plot
for group_index in range(num_groups):
    fig, axes = plt.subplots(4, 1, figsize=(16, 8))
    
    if group_index < len(front_right_grouped_data):
        ax1 = axes[0]
        group = front_right_grouped_data[group_index]
        for i, (timestamp, temp) in enumerate(group):
            ax1.text(i, 0.6, f'{temp:.1f}°C', fontsize=12, ha='center', va='center')
            ax1.text(i, 0.4, f'{timestamp}', fontsize=8, ha='center', va='center')
        ax1.set_xlim(-0.5, 15.5)
        ax1.set_ylim(0, 1)
        ax1.set_aspect('equal', adjustable='box')
        ax1.set_xticks([])
        ax1.set_yticks([])
        ax1.set_title('Front Right Tire')
        ax1.grid(True)
    
    if group_index < len(front_left_grouped_data):
        ax2 = axes[1]
        group = front_left_grouped_data[group_index]
        for i, (timestamp, temp) in enumerate(group):
            ax2.text(i, 0.6, f'{temp:.1f}°C', fontsize=12, ha='center', va='center')
            ax2.text(i, 0.4, f'{timestamp}', fontsize=8, ha='center', va='center')
        ax2.set_xlim(-0.5, 15.5)
        ax2.set_ylim(0, 1)
        ax2.set_aspect('equal', adjustable='box')
        ax2.set_xticks([])
        ax2.set_yticks([])
        ax2.set_title('Front Left Tire')
        ax2.grid(True)
    
    if group_index < len(rear_left_grouped_data):
        ax3 = axes[2]
        group = rear_left_grouped_data[group_index]
        for i, (timestamp, temp) in enumerate(group):
            ax3.text(i, 0.6, f'{temp:.1f}°C', fontsize=12, ha='center', va='center')
            ax3.text(i, 0.4, f'{timestamp}', fontsize=8, ha='center', va='center')
        ax3.set_xlim(-0.5, 15.5)
        ax3.set_ylim(0, 1)
        ax3.set_aspect('equal', adjustable='box')
        ax3.set_xticks([])
        ax3.set_yticks([])
        ax3.set_title('Rear Left Tire')
        ax3.grid(True)
    
    if group_index < len(rear_right_grouped_data):
        ax4 = axes[3]
        group = rear_right_grouped_data[group_index]
        for i, (timestamp, temp) in enumerate(group):
            ax4.text(i, 0.6, f'{temp:.1f}°C', fontsize=12, ha='center', va='center')
            ax4.text(i, 0.4, f'{timestamp}', fontsize=8, ha='center', va='center')
        ax4.set_xlim(-0.5, 15.5)
        ax4.set_ylim(0, 1)
        ax4.set_aspect('equal', adjustable='box')
        ax4.set_xticks([])
        ax4.set_yticks([])
        ax4.set_title('Rear Right Tire')
        ax4.grid(True)
    
    plt.tight_layout()
    plt.pause(2)  # Display the plot for 2 seconds
    plt.close()

# Check if any temperatures were extracted
if not front_right_tire_data:
    print("No temperatures extracted for Front Right Tire. Please check the input file and the regex pattern.")
if not front_left_tire_data:
    print("No temperatures extracted for Front Left Tire. Please check the input file and the regex pattern.")
if not rear_left_tire_data:
    print("No temperatures extracted for Rear Left Tire. Please check the input file and the regex pattern.")
if not rear_right_tire_data:
    print("No temperatures extracted for Rear Right Tire. Please check the input file and the regex pattern.")
