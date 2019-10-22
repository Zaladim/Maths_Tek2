def usage():
	print("USAGE")
	print("\t./207demography code [...]\n")
	print("DESCRIPTION")
	print("\tcode\tcountry code")
	return 0

def argError(argv):
	if len(argv) < 2:
		return True
	return False