import error
import numpy as np

def start(argv):
	if (error.argError(argv)):
		error.usage()
		return 84
	sample(argv)
	v = variance(argv)
	confidence(v, float(argv[3]))
	

def sample(argv):
	print("Population size:\t%d" %int(argv[1]))
	print("Sample size:\t%d" %int(argv[2]))
	print("Voting intention:\t%.2f%%" %float(argv[3]))

def variance(argv):
	pSize = int(argv[1])
	sSize = int(argv[2])
	p = float(argv[3]) / 100
	v = ((p * (1 - p)) / sSize)
	v *= ((pSize - sSize) / (pSize - 1))
	v = ((p * (1 - p)) / sSize) * ((pSize - sSize) / (pSize - 1))
	print("Variance:\t%.6f" %v)
	return v

def confidence(v, p):
	c1 = (2 * 1.96 * np.sqrt(v)) * 50
	c2 = (2 * 2.58 * np.sqrt(v)) * 50
	print("95%% confidence interval:\t[%.2f%%; %.2f%%]" %(max((p - c1), 0), min((p + c1), 100)))
	print("99%% confidence interval:\t[%.2f%%; %.2f%%]" %(max((p - c2), 0), min((p + c2), 100)))