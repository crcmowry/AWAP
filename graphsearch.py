### example input
# a = [[5, 1, 2, 3], 
# 	[1, 1, 100, 5],
# 	[200, 3, 1, 4]]
# b = (2, 2)

### example output
# [[(10, (1, 0)), (5, (1, 1)), (7, (0, 1)), (10, (0, 2))],
# [(5, (1, 1)), (4, (2, 1)), (100, (2, 2)), (9, (2, 3))],
# [(203, (2, 1)), (3, (2, 2)), (0, (2, 2)), (4, (2, 2))]]

###input of matrix of costs, and starting vertex
def search(M, start):
	(h, w) = start
	height = len(M)
	width = len(M[0])
	visited = set()
	minpath = [[(-1, (0,0)) for i in range (width)] for j in range (height)]
	minpath[h][w] = (0, (h,w))
	unvisited = {0:[(h,w)]}
	total = height * width
	while (len(visited) < total):
		key = sorted(unvisited)
		lowest = unvisited[key[0]]
		(h,w) = lowest[0]
		lowest.remove((h,w))
		if lowest == []:
			del unvisited[key[0]]
		else:
			unvisited[key[0]] = lowest
		visited.add((h,w))
		neighbors = [(h, w-1), (h-1, w), (h, w+1), (h+1, w)]
		for n in neighbors:
			(i, j) = n
			if i >= 0 and i < height:
				if j >= 0 and j < width:
					oldV = minpath[i][j][0]
					newV = minpath[h][w][0] + M[i][j]
					if oldV == -1:
						minpath[i][j] = (newV, (h, w))
						tmp = unvisited.get(newV, [])
						tmp.append((i,j))
						unvisited[newV] = tmp
					elif newV < oldV:
						minpath[i][j] = (newV, (h, w))
						if (i,j) not in visited:
							unvisited[oldV].remove((i,j))
							tmp = unvisited.get(newV, [])
							tmp.append((i,j))
							unvisited[newV] = tmp
	return minpath
