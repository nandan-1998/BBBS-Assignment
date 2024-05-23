import numpy as np
from scipy import signal

# Load the data from the file
samplefile = 'sample_bbbs_assignment_id100.dat'
with open(samplefile, "rb") as f:
    data = np.fromfile(f, dtype=np.float64)  # Ensure the dtype matches the file

# Set the sampling rate
sampling_rate = 50e6  # 50 Msps

# Nyquist rate
nyquist_rate = sampling_rate / 2

# Debugging function to check cutoff frequencies
def check_cutoff_frequencies(lower, upper):
    print(f"Normalized lower cutoff: {lower}, Normalized upper cutoff: {upper}")
    if not (0 < lower < 1) or not (0 < upper < 1):
        raise ValueError(f"Invalid cutoff frequencies: {lower}, {upper}")

# 1. Extract the packet with duration 581 microseconds and bandwidth 10 MHz
packet_duration_1 = 581e-6  # 581 microseconds
packet_bandwidth_1 = 10e6  # 10 MHz

# Design an FIR bandpass filter for packet 1
center_freq_1 = 20e6  # Center frequency: 20 MHz
lower_cutoff_1 = center_freq_1 - packet_bandwidth_1 / 2  # Lower cutoff: 15 MHz
upper_cutoff_1 = center_freq_1 + packet_bandwidth_1 / 2  # Upper cutoff: 25 MHz
normalized_lower_cutoff_1 = lower_cutoff_1 / nyquist_rate
normalized_upper_cutoff_1 = upper_cutoff_1 / nyquist_rate

# Ensure upper cutoff frequency is strictly less than 1
if normalized_upper_cutoff_1 >= 1:
    normalized_upper_cutoff_1 = 0.999

# Check cutoff frequencies for packet 1
check_cutoff_frequencies(normalized_lower_cutoff_1, normalized_upper_cutoff_1)

filter_order_1 = 100
filter_coeffs_1 = signal.firwin(filter_order_1 + 1, [normalized_lower_cutoff_1, normalized_upper_cutoff_1], pass_zero=False)

# Apply the filter and extract the packet
filtered_data_1 = signal.lfilter(filter_coeffs_1, [1.0], data)
num_samples_1 = int(packet_duration_1 * sampling_rate)
start_idx_1 = 0  # Assuming the packet starts at the beginning of the data
end_idx_1 = start_idx_1 + num_samples_1
packet_1 = filtered_data_1[start_idx_1:end_idx_1]

# 2. Extract the packet with duration 5.08 ms and bandwidth 20 MHz
packet_duration_2 = 5.08e-3  # 5.08 milliseconds
packet_bandwidth_2 = 20e6  # 20 MHz

# Design an FIR bandpass filter for packet 2
center_freq_2 = 30e6  # Center frequency: 30 MHz
lower_cutoff_2 = center_freq_2 - packet_bandwidth_2 / 2  # Lower cutoff: 20 MHz
upper_cutoff_2 = center_freq_2 + packet_bandwidth_2 / 2  # Upper cutoff: 40 MHz
normalized_lower_cutoff_2 = lower_cutoff_2 / nyquist_rate
normalized_upper_cutoff_2 = upper_cutoff_2 / nyquist_rate

# Ensure upper cutoff frequency is strictly less than 1
if normalized_upper_cutoff_2 >= 1:
    normalized_upper_cutoff_2 = 0.999

# Check cutoff frequencies for packet 2
check_cutoff_frequencies(normalized_lower_cutoff_2, normalized_upper_cutoff_2)

filter_order_2 = 100
filter_coeffs_2 = signal.firwin(filter_order_2 + 1, [normalized_lower_cutoff_2, normalized_upper_cutoff_2], pass_zero=False)

# Apply the filter and extract the packets
filtered_data_2 = signal.lfilter(filter_coeffs_2, [1.0], data)
num_samples_2 = int(packet_duration_2 * sampling_rate)

# Assuming there are N packets present in the sample
N = 10  # Replace with the actual number of packets
packets_2 = []
for i in range(N):
    start_idx_2 = i * num_samples_2
    end_idx_2 = start_idx_2 + num_samples_2
    # Ensure we do not go out of the bounds of the data array
    if end_idx_2 <= len(filtered_data_2):
        packet = filtered_data_2[start_idx_2:end_idx_2]
        packets_2.append(packet)

# Save the extracted packets to files (optional)
# np.save('packet_1.npy', packet_1)
# np.savez('packets_2.npz', *packets_2)

# Print the shapes of the extracted packets
print(f"Shape of packet 1: {packet_1.shape}")
print(f"Shapes of packets 2: {[packet.shape for packet in packets_2]}")
