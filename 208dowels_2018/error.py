def usage():
    print("USAGE")
    print("\t./207dowels 00 01 02 03 04 05 06 07 08 09\n")
    print("DESCRIPTION")
    print("\t0i\tsize of the observed class")
    return 0

def argError(argv):
    cpt = 0

    if len(argv) != 10:
        return True
    try:
        for i in range(1, 10):
            if (int(argv[i]) <= 0.0):
                return True
            cpt += int(argv[i])
    except ValueError:
        return True
    if (cpt != 100):
        return True
    return False