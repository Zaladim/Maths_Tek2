##
## EPITECH PROJECT, 2019
## 201YAMS
## File description:
## Operations
##

import math

val = 6
elements = 5.0
prob = 1/val

def permutation(n):
	return math.factorial(n)

def combination(k, n):
	return (math.facctorial(n)/((math.factorial(k))*(math.factorial(n - k))))