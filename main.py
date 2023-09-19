import time
import board
import busio
import adxl355
import numpy as np
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

# Create an I2C object.
i2c = busio.I2C(board.SCL, board.SDA)

# Create an ADXL355 object.
adxl355 = adxl355.ADXL355(i2c)

# Collect the tri-axis acceleration data.
x_axis = adxl355.x
y_axis = adxl355.y
z_axis = adxl355.z

# Load the raw acceleration data into a numpy array.
raw_data = np.array([x_axis, y_axis, z_axis])

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


"""
This code will perform all of the steps necessary to visualize and acquire the natural frequency of a concrete structure from collected raw tri-axis acceleration data:

Collect the tri-axis acceleration data from the ADXL355 accelerometer.
Preprocess the data by removing the mean and filtering the data with a butterworth low-pass filter.
Convert the data to the frequency domain using the Fast Fourier Transform (FFT).
Visualize the data by plotting the magnitude of the FFT spectrum.
Acquire the natural frequency by finding the peak in the FFT spectrum.
You can use this code as a starting point to develop your own code for acquiring the natural frequency of a concrete structure.

"""