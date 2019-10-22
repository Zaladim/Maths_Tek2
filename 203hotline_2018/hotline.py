import time
import math
import error
import sys
import globalVariable as gv

def binCoef(n, k):
	if (n == k):
		return 1
	if (k == 1):
		return n
	if (k == 0):
		return 1
	if (k > n):
		return 0
	if (k < 0):
		return -1
	return binCoef(n - 1, k - 1) * n // k

# def binomial(x):

def getLambda(d):
	sec = gv.H * gv.SEC_CONV
	return gv.NB * d / sec

def probability(d):
	return (d / float(gv.H * gv.SEC_CONV))

def binomial(d):
	start = time.time()
	p = probability(d)
	overload = 0.0
	print("Binomial distribution:")
	for n in range(0, 51):
		prob = (binCoef(gv.NB, n) * (p**n) * ((1 - p)**(gv.NB - n)))
		print("%d -> %0.3f" %(n, prob), end = "")
		if ((n + 1) % 6 == 0 or n == 50):
			print("")
		else:
			print("", end = "\t")
		if (n > 25):
			overload += prob
	n = 51
	prob = (binCoef(gv.NB, n) * (p**n) * ((1 - p)**(gv.NB - n)))
	while (prob > 0.000001 and overload < 1):
		n += 1
		overload += prob
		prob = (binCoef(gv.NB, n) * (p**n) * ((1 - p)**(gv.NB - n)))
	if (overload < 0.1 and p > 0.01):
		overload = 1
	print("overload:  %0.1f%%" %(overload * 100))
	end = time.time()
	print("computation time:  %0.2f ms" %((end - start) * 1000))

def poisson(d):
	start = time.time()
	l = getLambda(d)
	overload = 0.0
	print("Poisson distribution:")
	for n in range(0, 51):
		prob = ((math.exp(-l) * (l**n)) / math.factorial(n))
		print("%d -> %0.3f" %(n, prob), end = "")
		if ((n + 1) % 6 == 0 or n == 50):
			print("")
		else:
			print("", end = "\t")
		if (n > 25):
			overload += prob
	n = 51.0
	prob = ((math.exp(-l) * (l**n)) / math.factorial(n))
	while (prob > 0.000001 and overload < 1):
		n += 1
		overload += prob
		prob = ((math.exp(-l) * (l**n)) / math.factorial(n))
	if (overload < 0.1 and l > 50.0):
		overload = 1
	print("overload:  %0.1f%%" %(overload * 100))
	end = time.time()
	print("computation time:  %0.2f ms" %((end - start) * 1000))


def start(argv):
	if (error.argError(argv)):
		return 84
	if (len(argv) == 3):
		if (int(argv[1]) < 0 or int(argv[2]) < 0):
			return 84
		print(argv[2] + "-combination of a " + argv[1] + " set:")
		coef = binCoef(int(argv[1]), int(argv[2]))
		if (coef >= 0):
			print("%d"% binCoef(int(argv[1]), int(argv[2])))
			return 0
		else:
			return 84
	if (len(argv) == 2):
		if (int(argv[1]) < 0):
			return 84
		binomial(int(argv[1]))
		print("")
		poisson(int(argv[1]))
		return 0