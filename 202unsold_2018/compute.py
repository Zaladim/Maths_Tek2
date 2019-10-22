import globalVariable as va

def joint(a, b, x, y):
	return ((a - x)*(b - y))/((5 * a - 150) * (5 * b - 150))

def marginalX(a, b, x):
	ret = 0
	for elem in va.Y:
		ret += joint(a, b, x, elem)
	return ret

def marginalY(a, b, y):
	ret = 0
	for elem in va.X:
		ret += joint(a, b, elem, y)
	return ret

def lawZ(a, b, z):
	ret = 0
	val = []
	for x in va.X:
		for y in va.Y:
			if (x + y == z):
				val.append((x, y))
	for elem in val:
		ret += joint(a, b, elem[0], elem[1])
	return ret

def expected(list, law):
	ret = 0
	size = len(list)
	for elem in range(0, size):
		ret += (list[elem] * law[elem])
	return ret

def variance(list, law):
	ret = 0
	size = len(list)
	for elem in range(0, size):
		ret += (list[elem] ** 2 * law[elem])
	return ret - (expected(list, law) ** 2)