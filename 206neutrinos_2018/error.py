def usage():
	print("USAGE")
	print("\t./206neutrinos n a h sd\n")
	print("DESCRIPTION")
	print("\tn\tnumber of values")
	print("\ta\tarithmetic mean")
	print("\th\tharmonic mean")
	print("\tsd\tstandard deviation")
	return 0

def argError(argv):
	if len(argv) != 5:
		return True
	try:
		for i in range(1, 5):
			if (float(argv[i]) < 0.0):
				return True
		if (float(argv[3]) == 0.0):
			return True
	except ValueError:
		return True
	return False