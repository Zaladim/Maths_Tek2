##
## EPITECH PROJECT, 2019
## 201YAMS
## File description:
## Operations
##

import math

def permutation(n):
	return math.factorial(n)

def combination(k, n):
	return (math.factorial(n)/((math.factorial(k))*(math.factorial(n - k))))