import numpy as np

def fit1(pop):
    print("Fit1")
    (ax, bx) = get_coef(pop)
    if (bx >= 0): 
        print ("\tY = %.2f X + %.2f" % (ax, bx))
    else:
        print ("\tY = %.2f X - %.2f" % (ax, (bx * -1)))
    print("\tRoot-mean-square deviation: %.2f" %root_mean(ax, bx, pop))
    print("\tPopulation in 2050: %.2f" %(ax * 2050 + bx))
    return ax

def get_coef(pop):
    num = 0
    denum = 0
    year = 1960
    averageYear = 0
    averagePop = 0
    for i in range(0, len(pop)):
        num += year * (pop[i] / 10**6)
        denum += year**2
        averageYear += year
        averagePop += (pop[i] / 10**6)
        year += 1
    averageYear /= (len(pop))
    averagePop /= (len(pop))
    num -= len(pop) * averageYear * averagePop
    denum -= len(pop) * averageYear**2
    ax = num/denum
    return (ax, averagePop - ax * averageYear)

def root_mean(ax, bx, pop):
    root = 0.0
    year = 1960
    for i in range(0, len(pop)):
        root += ((pop[i] / 10**6) - (bx + ax * year))**2
        year += 1
    return np.sqrt (root / len(pop))