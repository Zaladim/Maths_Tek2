##
## EPITECH PROJECT, 2019
## 201YAMS
## File description:
## Combination
##

import math
import operation as op


def yams(dice, A):
	die = 5
	need = 5

	for elem in dice:
		if (elem == A):
			die -= 1
			need -= 1
	if (need <= 0):
		return 1
	
	return ((op.combination(need, die) * (op.prob ** die)))

def four(dice, A):
	die = 5
	need = 4

	for elem in dice:
		if (elem == A):
			die -= 1
			need -= 1
	if (need <= 0):
		return 1
	
	return ((op.combination(need, die) * (op.prob ** need) * ((1 - op.prob) ** (die - need))) + yams(dice, A))

def three(dice, A):
	die = 5
	need = 3

	for elem in dice:
		if (elem == A):
			die -= 1
			need -= 1
	if (need <= 0):
		return 1
	
	return ((op.combination(need, die) * (op.prob ** need) * ((1 - op.prob) ** (die - need))) + four(dice, A))

def pair(dice, A):
	die = 5
	need = 2

	for elem in dice:
		if (elem == A):
			die -= 1
			need -= 1
	if (need <= 0):
		return 1
	
	return ((op.combination(need, die) * (op.prob ** need) * ((1 - op.prob) ** (die - need))) + three(dice, A))

def full(dice, A, B):
	reroll = 5
	cptA = 0
	cptB = 0

	for elem in dice:
		if (elem == A and cptA < 3):
			reroll -= 1
			cptA += 1
		if (elem == B and cptB < 2):
			reroll -= 1
			cptB += 1
	return (op.combination((2-cptB), reroll) / (op.val ** reroll))

def straight(dice, A):
	perm = 5

	for elem in dice:
		try:
			dice.index(A)
		except ValueError:
			A -= 1
		else:
			A -= 1
			perm -= 1
	if (perm <= 0):
		return 1	
	
	return (op.permutation(perm) / (op.val ** perm))