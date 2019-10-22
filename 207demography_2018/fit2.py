import numpy as np

def fit2(pop):
    print("Fit2")
    (ay, by) = get_coef(pop)
    if (by >= 0): 
        print ("\tX = %.2f Y + %.2f" % (ay, by))
    else:
        print ("\tX = %.2f Y - %.2f" % (ay, (by * -1)))
    print("\tRoot-mean-square deviation: %.2f" %root_mean(ay, by, pop))
    print("\tPopulation in 2050: %.2f" %((2050- by) / ay))
    return ay

def get_coef(pop):
    num = 0
    denum = 0
    year = 1960
    averageYear = 0
    averagePop = 0
    for i in range(0, len(pop)):
        averageYear += year
        averagePop += (pop[i] / 10**6)
        year += 1
    averageYear /= len(pop)
    averagePop /= len(pop)
    year = 1960
    for i in range(0, len(pop)):
        num += (year - averageYear) * ((pop[i] / 10**6) - averagePop)
        denum += ((pop[i] / 10**6) - averagePop)**2
        year += 1
    ay = num / denum
    return (ay, averageYear - ay * averagePop)

def root_mean(ay, by, pop):
    root = 0.0
    year = 1960
    for i in range(0, len(pop)):
        root += ((pop[i] / 10**6) - ((year - by) / ay))**2
        year += 1
    return np.sqrt (root / len(pop))