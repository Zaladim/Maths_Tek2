def usage():
	print("USAGE")
	print("\t./205IQ u s [IQ1] [IQ2]\n")
	print("DESCRIPTION")
	print("\tu\tmean")
	print("\ts\tstandard deviation")
	print("\tIQ1\tminimum IQ")
	print("\tIQ2\tmaximum IQ")
	return 0

def argError(argv):
	if len(argv) < 3 or len(argv) > 5:
		return True
	try:
		if (int(argv[1]) < 0 or int(argv[1]) > 200):
			usage()
			return True
		if float(argv[2]) <= 0:
			usage()
			return True
		if (len(argv) == 4 and (int(argv[3]) < 0 or int(argv[3]) > 200)):
			usage()
			return True
		if (len(argv) == 5 and (int(argv[4]) < 0 or int(argv[4]) > 200)):
			usage()
			return True
	except ValueError:
		usage()
		return True
	return False