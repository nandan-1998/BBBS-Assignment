# BBBS-Assignment
# Signal Packet Extraction

This Python script is designed to extract signal packets from a provided IQ sample data file. The script supports extracting two sets of packets with different durations and bandwidths using FIR bandpass filtering.

## Requirements

- Python 3.10
- NumPy
- SciPy

## Usage
1. Make sure you have the required Python packages installed.
2. Place the IQ sample data file (`sample_bbbs_assignment_id100.dat`) in the same directory as the script.
3. Open the script in a text editor or Python IDE.
4. Replace the value of `N` with the actual number of packets present in the second set of packets.
5. Run the script.

The script will perform the following tasks:

1. Load the IQ sample data from the `sample_bbbs_assignment_id100.dat` file.
2. Design and apply an FIR bandpass filter to extract the first packet with a duration of 581 microseconds and a bandwidth of 10 MHz, centered around 20 MHz.
3. Design and apply an FIR bandpass filter to extract the second set of packets, each with a duration of 5.08 milliseconds and a bandwidth of 20 MHz, centered around 30 MHz.
4. Print the shapes (dimensions) of the extracted packets.

## Code Explanation

The script follows these steps:

1. Import the required Python libraries: NumPy and SciPy.
2. Load the IQ sample data from the specified file (`sample_bbbs_assignment_id100.dat`) using `np.fromfile`.
3. Set the sampling rate to 50 MHz.
4. Calculate the Nyquist rate based on the sampling rate.
5. Define a function `check_cutoff_frequencies` to ensure that the normalized cutoff frequencies are within the valid range of 0 to 1.
6. For the first packet:
   - Calculate the center frequency, lower cutoff, and upper cutoff frequencies based on the specified bandwidth.
   - Ensure the upper cutoff frequency is strictly less than 1.
   - Check the cutoff frequencies using `check_cutoff_frequencies`.
   - Design an FIR bandpass filter using `signal.firwin`.
   - Apply the filter to the IQ data using `signal.lfilter`.
   - Extract the packet by windowing the filtered data based on the specified duration.
7. For the second set of packets:
   - Calculate the center frequency, lower cutoff, and upper cutoff frequencies based on the specified bandwidth.
   - Ensure the upper cutoff frequency is strictly less than 1.
   - Check the cutoff frequencies using `check_cutoff_frequencies`.
   - Design an FIR bandpass filter using `signal.firwin`.
   - Apply the filter to the IQ data using `signal.lfilter`.
   - Extract the packets by windowing the filtered data based on the specified duration, with a loop to handle multiple packets.
   - Include a check to ensure the end index does not go out of bounds of the filtered data array.
9. Print the shapes (dimensions) of the extracted packets.

