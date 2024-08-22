import time

def get_result_slower(n: int, k: int) -> int:
	start = time.time()
	nc = n
	rows = []
	rows.append([1] * (nc + 1))
	for _ in range(k):
		rows.append([0] * (nc))
		nc -= 1
	for x in range(1, k + 1):
		rows[x][0] = 1
		nc = len(rows[x])
		for y in range(1, nc):
			rows[x][y] = rows[x][y - 1] + rows[x - 1][y]
		nc -= 1
	end = time.time()
	print(end - start)
	return rows[-1][-1]

print(get_result_slower(10000, 88))

def get_result(n: int, k: int) -> int:
	start = time.time()
	if n < 2 * k:
		k = n - k
	rows = []
	rows.append([1] * (n + 1))
	for i in range(k):
		rows.append([0] * (n - i))
	for x in range(1, k + 1):
		rows[x][0] = 1
		for y in range(1, len(rows[x])):
			rows[x][y] = rows[x][y - 1] + rows[x - 1][y]
	end = time.time()
	print(end - start)
	return rows[-1][-1]

print(get_result(10000, 88))