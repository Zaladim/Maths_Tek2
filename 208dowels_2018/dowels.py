import error
import operation as op
import numpy as np

def start(argv):
    if (error.argError(argv)):
        error.usage()
        return 84
    p = probability(argv)
    (Ox, Tx) = show_array(argv, p)
    distribution(p)
    chi = chi2(Ox, Tx)
    free = freedom(len(Ox))
    validity(chi, free)
    return 0

def distribution(p):
    print("Distribution:\tB(100, %.4f)" %p)

def chi2(Ox, Tx):
    chi = 0

    for i in range(0, len(Ox)):
        chi += np.power(Ox[i] - Tx[i], 2) / Tx[i]
    print("Chi-squared:\t%.3f" %chi)
    return chi

def freedom(len):
    print("Degrees of freedom:\t%d"%(len - 2))
    return len - 2

def validity(chi, free):
    max = 1
    min = 0
    data = [[99, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 3, 1],
    [0.00, 0.02, 0.06, 0.15, 0.27, 0.45, 0.71, 1.07, 1.64, 2.71, 3.84, 5.41, 6.63],
    [0.02, 0.21, 0.45, 0.71, 1.02, 1.39, 1.83, 2.41, 3.22, 4.61, 5.99, 7.82, 9.21],
    [0.11, 0.58, 1.01, 1.42, 1.87, 2.37, 2.95, 3.66, 4.64, 6.25, 7.81, 9.84, 11.34],
    [0.30, 1.06, 1.65, 2.19, 2.75, 3.36, 4.04, 4.88, 5.99, 7.78, 9.49, 11.67, 13.28],
    [0.55, 1.61, 2.34, 3.00, 3.66, 4.35, 5.13, 6.06, 7.29, 9.24, 11.07, 13.39, 15.09],
    [0.87, 2.20, 3.07, 3.83, 4.57, 5.35, 6.21, 7.23, 8.56, 10.64, 12.59, 15.03, 16.81],
    [1.24, 2.83, 3.82, 4.67, 5.49, 6.35, 7.28, 8.38, 9.80, 12.02, 14.07, 16.62, 18.48],
    [1.65, 3.49, 4.59, 5.53, 6.42, 7.34, 8.35, 9.52, 11.03, 13.36, 15.51, 18.17, 20.09],
    [2.09, 4.17, 5.38, 6.39, 7.36, 8.34, 9.41, 10.66, 12.24, 14.68, 16.92, 19.68, 21.67],
    [2.56, 4.87, 6.18, 7.27, 8.30, 9.34, 10.47, 11.78, 13.44, 15.99, 18.31, 21.16, 23.21]]

    for i in range(0, len(data[0]) - 1):
        if (chi < data[free][i]):
            if (i > 0):
                max = data[0][i - 1]
            else:
                max = 0
            min = data[0][i]
            break

    if (max == 1):
        print("Fit validity:\tP < 1%")
    elif (min == 99):
        print("Fit validity:\tP > 99%")
    else:
        print("Fit validity:\t%d%% < P < %d%%" %(min, max))


def show_array(argv, p):
    tmp = 0
    res = 0
    i = 1
    last = 0
    Ox = []
    Tx = []

    print(f"{'x':>4}\t|", end = " ")
    while i < 9:
        if (i == 1):
            print(" %d" %(i - 1), end = "")
        elif (tmp == 0 and (int(argv[i - 1]) != 0)):
            print("%d" %(i - 1), end = "")
            last = i - 1
        tmp += int(argv[i])
        res += 100 * op.combination(i - 1, 100) * np.power(p, i - 1) * np.power((1 - p), 100 - (i - 1))
        if (tmp >= 10 and (int(argv[i + 1]) >= 10)):
            if (tmp != int(argv[i]) or int(argv[i - 1] == 0)):
                print("-%d" %(i - 1), end = "")
                last = i - 1
            print("\t|", end = " ")
            Ox.append(tmp)
            Tx.append(res)
            res = 0
            tmp = 0
        i += 1
    if (tmp != 0):
        print("\t|", end = " ")
        Ox.append(tmp - int(argv[i - 1]))
        res -= 100 * op.combination(i - 2, 100) * np.power(p, i - 2) * np.power((1 - p), 100 - (i - 2))
        Tx.append(res)
    print("%d+\t| Total" %(last + 1))

    tmp = 0
    print(f"{'Ox':>4}\t|", end = " ")
    for O in Ox:
        print(" %d\t|" %O, end = "")
    for i in range(last + 1, 9):
        tmp += int(argv[i + 1])
    print(" %d\t| 100" %tmp)
    Ox.append(tmp)

    tmp = 0
    print(f"{'Tx':>4}\t|", end = " ")
    for T in Tx:
        print(" %.1f\t|" %T, end = "")
        tmp += T
    print(" %.1f\t| 100" %(100 - tmp))
    Tx.append(100 - tmp)
    
    return (Ox, Tx)

def probability(argv):
    p = 0
    for i in range(1, 10):
        p += float(argv[i]) * (i - 1)
    return (p / 10000.0)