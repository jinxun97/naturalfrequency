import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter


# Create a list of tri-axis acceleration data
tri_axis_acceleration_data = [[0.0, 0.0, 0.0], [0.01, 0.01, 0.3], [0.02, 0.02, 0.02], [0.03, 0.03, 0.03], [0.04, 9, 0.04], [0.05, 0.9, 0.05], [0.06, 100, 0.06], [0.07, 0.07, 0.07], [0.08, 0.08, 0.08], [0.09, 0.09, 0.09], [0.1, 0.1, 0.1]]

# Convert the tri-axis acceleration data to a NumPy array
tri_axis_acceleration_data = np.array(tri_axis_acceleration_data)

# Remove the mean from the data
mean = np.mean(tri_axis_acceleration_data, axis=0)
normalized_data = tri_axis_acceleration_data - mean

# Design a butterworth low-pass filter with a cutoff frequency of 10 Hz
b, a = butter(4, 10 / (0.5 * 250), btype="lowpass")

# Apply the filter to the data
filtered_data = lfilter(b, a, normalized_data)

# Calculate the FFT of the filtered data
fft_data = np.fft.fft(filtered_data)

# Calculate the magnitude of the FFT data for each axis of acceleration
magnitude_x = np.abs(fft_data[0, :])
magnitude_y = np.abs(fft_data[1, :])
magnitude_z = np.abs(fft_data[2, :])

# Plot the magnitude of the FFT spectrum for each axis of acceleration
plt.plot(np.arange(len(magnitude_x)) * (250 / len(magnitude_x)), magnitude_x, label="X-axis acceleration")
plt.plot(np.arange(len(magnitude_y)) * (250 / len(magnitude_y)), magnitude_y, label="Y-axis acceleration")
plt.plot(np.arange(len(magnitude_z)) * (250 / len(magnitude_z)), magnitude_z, label="Z-axis acceleration")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("FFT Spectrum of Tri-Axis Acceleration Data")
plt.legend()
plt.show()


"""
This code will perform all of the steps necessary to visualize and acquire the natural frequency of a concrete structure from collected raw tri-axis acceleration data:

Collect the tri-axis acceleration data from the ADXL355 accelerometer.
Preprocess the data by removing the mean and filtering the data with a butterworth low-pass filter.
Convert the data to the frequency domain using the Fast Fourier Transform (FFT).
Visualize the data by plotting the magnitude of the FFT spectrum.
Acquire the natural frequency by finding the peak in the FFT spectrum.
You can use this code as a starting point to develop your own code for acquiring the natural frequency of a concrete structure.

"""