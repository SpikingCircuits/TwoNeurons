import serial
import time
import numpy as np

ser = serial.Serial('/dev/tty.usbmodemfa131', 38400)

time.sleep(1)

# Send a list of spikes and blink at each spike 
def send_list(input_spikes,output_spikes,dec_factor):

	# Time array creation
	max_time = max(input_spikes)*dec_factor
	dt = 0.01*dec_factor
	time_array = np.arange(0,max_time+dt,dt)

	# Deccelerate spike times
	for i,item in enumerate(input_spikes):
		input_spikes[i] = input_spikes[i]*dec_factor

	for i,item in enumerate(output_spikes):
		output_spikes[i] = output_spikes[i]*dec_factor

	for t in time_array:

		# Wait
		time.sleep(dt*1e-3)

		if t in input_spikes:
			print "Input spike at time", t
			ser.write('3')

		if t in output_spikes:
			print "Output spike at time", t
			ser.write('2')

# Test the stuff

# Import results from pyNN
raw_list = np.genfromtxt("Results/spikes.dat")

output_spikes = []
for i in raw_list:
	output_spikes.append(i[0])

input_spikes = np.genfromtxt("Results/input_spikes.dat")

send_list(input_spikes,output_spikes,10)