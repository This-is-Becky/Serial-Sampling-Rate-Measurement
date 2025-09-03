# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 14:53:48 2023

@author: beckylin
"""

import serial
import time

# Configure your serial port settings

# Change to your actual port, e.g., '/dev/ttyUSB0' on Linux
SERIAL_PORT = 'COM16'  
#Change the baud rate according to the setting
BAUD_RATE = 115200
MEASUREMENT_DURATION = 10  # seconds

# Open the serial port
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

# Start measuring
start_time = time.time()
sample_count = 0

print(f"Measuring sampling rate for {MEASUREMENT_DURATION} seconds...")

while time.time() - start_time < MEASUREMENT_DURATION:
    if ser.in_waiting:
        data = ser.readline()
        sample_count += 1

# Close the serial port
ser.close()

# Calculate sampling rate
elapsed_time = time.time() - start_time
sampling_rate = sample_count / elapsed_time

print(f"Total samples received: {sample_count}")
print(f"Elapsed time: {elapsed_time:.2f} seconds")
print(f"Sampling rate: {sampling_rate:.2f} samples/second")

