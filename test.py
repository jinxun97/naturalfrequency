import time
##import board
##import busio
##import adxl355
import numpy as np
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt
import csv

"""# Create an I2C object.
i2c = busio.I2C(board.SCL, board.SDA)

# Create an ADXL355 object.
adxl355 = adxl355.ADXL355(i2c)"""

# Create a list of tri-axis acceleration data
tri_axis_acceleration_data = [[0.0, 0.0, 0.0], [0.01, 0.01, 0.01], [0.02, 0.02, 0.02], [0.03, 0.03, 0.03], [0.04, 1, 0.04], [0.05, 0.9, 0.05], [0.06, 0.06, 0.06], [0.07, 0.07, 0.07], [0.08, 0.08, 0.08], [0.09, 0.09, 0.09], [0.1, 0.1, 0.1]]

# Open a CSV file for writing
with open("tri_axis_acceleration_data.csv", "w", newline="") as f:
    writer = csv.writer(f)

    # Write the tri-axis acceleration data to the CSV file
    for row in tri_axis_acceleration_data:
        writer.writerow(row)

# Close the CSV file
f.close()

# Open the CSV acceleration data file for reading.
with open("tri_axis_acceleration_data.csv", "r") as f:
    reader = csv.reader(f)

    # Read the acceleration data from the CSV file into a NumPy array.
    raw_data = np.array([[row[0], row[1], row[2]] for row in reader])

# Create a list of the y-axis values for each axis of acceleration
y_x = [row[0] for row in tri_axis_acceleration_data]
y_y = [row[1] for row in tri_axis_acceleration_data]
y_z = [row[2] for row in tri_axis_acceleration_data]

# Create a figure and 3 subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1)

# Plot the x-axis acceleration data on the first subplot
ax1.plot(x, y_x, '.-', label='X-axis acceleration')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Acceleration (g)')
ax1.legend()

# Plot the y-axis acceleration data on the second subplot
ax2.plot(x, y_y, '.-', label='Y-axis acceleration')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Acceleration (g)')
ax2.legend()

# Plot the z-axis acceleration data on the third subplot
ax3.plot(x, y_z, '.-', label='Z-axis acceleration')
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Acceleration (g)')
ax3.legend()

# Tighten the layout of the figure
fig.tight_layout()

# Show the plot
plt.show()

# Convert the raw data to a numeric data type.
raw_data = raw_data.astype(np.float64)

# Remove the mean from the data.
mean = np.mean(raw_data, axis=0)
normalized_data = raw_data - mean

# Design a butterworth low-pass filter with a cutoff frequency of 10 Hz.
b, a = butter(4, 10 / (0.5 * 250), btype="lowpass")

# Apply the filter to the data.
filtered_data = lfilter(b, a, normalized_data)

# Calculate the FFT of the filtered data.
fft_data = np.fft.fft(filtered_data)

# Calculate the magnitude of the FFT data.
magnitude = np.abs(fft_data)

# Plot the magnitude of the FFT spectrum.
plt.plot(np.arange(len(magnitude)) * (250 / len(magnitude)), magnitude)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("FFT Spectrum of Tri-Axis Acceleration Data")
plt.show()

# Find the peak in the FFT spectrum.
peak_index = np.argmax(magnitude)

# Get the natural frequency of the concrete structure.
natural_frequency = peak_index * (250 / len(magnitude))

# Print the natural frequency of the concrete structure.
print("Natural frequency of the concrete structure:", natural_frequency, "Hz")
