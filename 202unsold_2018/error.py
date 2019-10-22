def usage():
	print("USAGE")
	print("\t./202unsold a b\n")
	print("DESCRIPTION")
	print("\ta\tconstant computed from the past results")
	print("\tb\tconstant computed from the past results")
	return 0

def argError(argv):
	try:
		if (len(argv) != 3):
			print("Invalid number of arguments")
			usage()
			return True
		if (int(argv[1]) < 50 or int(argv[2]) < 50):
			print("Arguments must be greather than 50")
			return True
	except ValueError:
		print("Arguments must be integers")
		return True
	else:
		return False