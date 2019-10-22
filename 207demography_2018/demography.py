import error
import fit1
import fit2
import numpy as np
import csv
import sys

def start(argv):
    country = []
    pop = []
    if (error.argError(argv)):
        error.usage()
        return 84
    with open('207demography_data.csv', 'r') as file:
        reader = csv.reader(file, delimiter = ';')
        for row in reader:
            try:
                argv.index(row[1])
            except ValueError:
                continue
            else:
                country.append(row)
        if (len(country) <= 0):
            print("No such country")
            return 84
        display_country(country)
        handle_pop(get_pop(country))
    return 0

def find_country(reader, code):
    for row in reader:
        if (row[1] == code):
            return row

def display_country(country):
    print("Country: ", end = "")
    for i in range(0, len(country)):
        print(country[i][0], end = "")
        if (i != len(country) - 1):
            print(", ", end = "")
        else:
            print("")

def get_pop(country):
    pop = []
    for i in range(2, len(country[0])):
        valYear = 0
        j = 0
        for j in range(0, len(country)):
            try:
                if country[j][i] != "":
                    valYear += float(country[j][i])
            except:
                valYear += 0
            j += 1
        pop.append(valYear)
        i += 1
    i = 0
    return (pop)


def handle_pop(pop):
    print("Correlation: %.4f" %(np.sqrt(fit1.fit1(pop) * fit2.fit2(pop))))


