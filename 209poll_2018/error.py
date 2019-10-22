def usage():
    print("USAGE")
    print("\t./209poll pSize sSize p\n")
    print("DESCRIPTION")
    print("\tpSize\tsize of the population")
    print("\tsSize\tsize of the sample (supposed to be representative)")
    print("\tp\tpercentage of voting intentions for a specific candidate")
    return 0

def argError(argv):
    cpt = 0

    if len(argv) != 4:
        return True
    try:
        for i in range(1, 3):
            if (int(argv[i]) <= 0):
                return True
        if (int(argv[1]) < 1):
            return True
        if (int(argv[2]) > int(argv[1])):
            return True
        if (float(argv[3]) < 0.0 or float(argv[3]) > 100.0 ):
            return True
    except ValueError:
        return True
    return False