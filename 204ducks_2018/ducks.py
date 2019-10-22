import error
import numpy as np

def fx(a, t):
	return a * np.exp(-t) + ((4 - 3 * a) * np.exp(-2 * t) + (2 * a - 4) * np.exp(-4 * t))

def start(argv):
	if (error.argError(argv)):
		return 84
	deviation(float(argv[1]), expected(float(argv[1])))
	if (time(float(argv[1]), 50) == -1):
		return 84
	if (time(float(argv[1]), 99) == -1):
		return 84
	percent(float(argv[1]), 1)
	percent(float(argv[1]), 2)
	return 0
	
def expected(a):
	ex = 0
	for t in np.arange(0, 50, 0.001):
		ex += (fx(a, t)) * t
	ex /= 1000
	ex += 1./60
	print("Average return time: %dm %02ds" % divmod(ex * 60, 60))
	return ex

def deviation(a, ex):
	sigma = 0
	for t in np.arange(0, 50, 0.01):
		sigma += (t - ex)**2 * fx(a, t)
	sigma /= 100
	sigma = np.sqrt(sigma)
	print("Standard deviation: %.3f" %sigma)

def time(a, val):
	res = 0
	t = 0.0
	for t in np.arange(0, 500, 0.01):
		res += fx(a, t)
		if res >= val:
			(m, s) = divmod(t * 60, 60)
			print("Time after which %d%% of the ducks are back: %dm %02ds" %(val, m, s))
			return t
		t += 1
	return -1

def percent(a, t):
	res = 0
	for i in np.arange(0, t, 0.0001):
		res += fx(a, i) / 100
	if t == 1:
		print("Percentage of ducks back after %d minute: %0.1f%%" %(t, res))
	else:
		print("Percentage of ducks back after %d minutes: %0.1f%%" %(t, res))

