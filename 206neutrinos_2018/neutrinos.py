import error
import numpy as np

def start(argv):
	if (error.argError(argv)):
		error.usage()
		return 84
	n = (float(argv[1]))
	a = (float(argv[2]))
	h = (float(argv[3]))
	sd = (float(argv[4]))
	next = read()
	while (next > 0):
		nr = rootMean(n, sd, a, next)
		na = arithmetic(n, a, next)
		nh = harmonic(n, h, next)
		nsd = deviation(n, a, sd, next)
		n += 1
		display(n, nsd, na, nr, nh)
		next = read()
		r = nr
		a = na
		h = nh
		sd = nsd
	return 0

def display(n, sd, a, r, h):
	print("\tNumber of values:\t%d" %n)
	print("\tStandard deviation:\t%.2f" %sd)
	print("\tArithmetic mean:\t%.2f" %a)
	print("\tRoot mean square:\t%.2f" %r)
	print("\tHarmonic mean:\t%.2f\n" %h)


def read():
	val = (input("Enter next value: "))
	try:
		return float(val)
	except ValueError:
		if (val == "END"):
			return 0
		print("Non valid value")
		return read()

def arithmetic(n, mean, new):
	a = (((n * mean) + new) / (n + 1))
	return a

def harmonic(n, mean, new):
	tmp = (n / mean)
	tmp = tmp + (1 / new)
	h = ((n + 1) / tmp)
	return h

def rootMean(n, sd, mean, new):
	tmp = ((sd**2) + (mean**2)) * n
	r = np.sqrt((tmp + (new**2)) / (n + 1))
	return r

def deviation(n, mean, sd, new):
	tmp = sd**2
	tmp = tmp * (n - 1)
	tmp += (new - mean)**2
	sd = (np.sqrt(tmp / n))
	return sd