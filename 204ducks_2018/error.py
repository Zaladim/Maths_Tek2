def usage():
	print("USAGE")
	print("\t./203ducks a\n")
	print("DESCRIPTION")
	print("\ta\tconstant")
	return 0

def argError(argv):
	if len(argv) != 2:
		return True
	try:
		if float(argv[1]) > 2.5 or float(argv[1]) < 0:
			return True
	except ValueError:
		return True
	return False