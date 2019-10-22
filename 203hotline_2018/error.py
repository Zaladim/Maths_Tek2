def usage():
	print("USAGE")
	print("\t./203hotline [n k | d]\n")
	print("DESCRIPTION")
	print("\tn\tn value for the computation of (nk)")
	print("\tk\tk value for the computation of (nk)")
	print("\td\taverage duration of calls (in seconds)")
	return 0

def argError(argv):
	if (len(argv) < 2 or len(argv) > 3):
		print("Invalid number of arguments")
		usage()
		return True
	try:
		int(argv[1])
		if (len(argv) == 3):
			int(argv[2])
	except ValueError:
		print("Arguments must be integers")
		return True
	return False