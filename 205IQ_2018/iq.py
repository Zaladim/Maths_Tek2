import error
import numpy as np

def fx(u, s, x):
	return (1 / (s * np.sqrt(2 * np.pi))) * np.exp(0 - (((x - u)**2) / (2 * (s**2))))

def start(argv):
	if (error.argError(argv)):
		return 84
	if len(argv) == 3:
		plot(argv)
	if len(argv) == 4:
		inf(float(argv[1]), float(argv[2]), int(argv[3]))
	if len(argv) == 5:
		between(float(argv[1]), float(argv[2]), int(argv[3]), int(argv[4]))
	return 0

def plot(argv):
	for x in range(0, 201):
		print("%d %.5f" %(x, fx(float(argv[1]), float(argv[2]), x)))

def inf(u, s, max):
	sum = 0
	for x in np.arange(0, max, 0.01):
		sum += fx(u, s, x)
	print("%0.1f%% of people have an IQ inferior to %d" %(sum, max))

def between(u, s, min, max):
	sum = 0
	for x in np.arange(min, max, 0.01):
		sum += fx(u, s, x)
	print("%0.1f%% of people have an IQ between %d and %d" %(sum, min, max))
