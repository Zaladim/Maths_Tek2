import math
import error
import compute as com
import globalVariable as va

def display(x):
	return (f'{x:.3f}')

def line():
	for i in range(0, 60):
		print('-', end = "")
	print()

def jointLaw(a, b):
	xLaw = []
	yLaw = []
	for elem in va.X:
		xLaw.append(com.marginalX(a, b, elem))
	for elem in va.Y:
		yLaw.append(com.marginalY(a, b, elem))
	print("\t", end = "")
	for elem in va.X:
		print("X=" + str(elem), end = "\t")
	print("Y law")
	for y in va.Y:
		print("Y=" + str(y), end = "\t")
		for x in va.X:
			print(display(com.joint(a, b, x, y)), end = "\t")
		print(display(com.marginalY(a, b, y)))
	print("X law", end = "\t")
	for elem in xLaw:
		print(display(elem), end = "\t")
	print(math.floor(math.ceil(sum(xLaw) + sum(yLaw))/2))
	return (xLaw, yLaw)

def ZArray(a, b):
	zLaw = []
	
	print("z", end = "\t")
	for z in va.Z:
		print(z, end = "\t")
	print("total")
	print("p(Z=z)", end = "\t")
	total = 0
	for z in va.Z:
		tmp = com.lawZ(a, b, z)
		total += tmp
		zLaw.append(tmp)
		print(display(tmp), end = "\t")
	print(int(total))
	return zLaw

def info(xLaw, yLaw, zLaw):
	print("expected value of X:", end = "\t")
	print(f'{com.expected(va.X, xLaw):.1f}')
	print("variance of X:", end = "\t\t")
	print(f'{com.variance(va.X, xLaw):.1f}')

	print("expected value of Y:", end = "\t")
	print(f'{com.expected(va.Y, yLaw):.1f}')
	print("variance of Y:", end = "\t\t")
	print(f'{com.variance(va.Y, yLaw):.1f}')

	print("expected value of Z:", end = "\t")
	print(f'{com.expected(va.Z, zLaw):.1f}')
	print("variance of Z:", end = "\t\t")
	print(f'{com.variance(va.Z, zLaw):.1f}')

def start(argv):
	if (error.argError(argv)):
		return 84
	line()
	(xLaw, yLaw) = jointLaw(int(argv[1]), int(argv[2]))
	line()
	zLaw = ZArray(int(argv[1]), int(argv[2]))
	line()
	info(xLaw, yLaw, zLaw)
	line()
	return 0