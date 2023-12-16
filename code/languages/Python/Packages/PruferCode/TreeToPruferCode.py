adjacency_list = {}
edge_num = int(input())
Prufer_code = []

for i in range(edge_num+1):
	adjacency_list[str(i)] = {"num": 0}    #Number of children of vertice i

for i in range(edge_num):
	father, child = input().split()
	adjacency_list[child]["father"] = father
	adjacency_list[father]["num"] += 1

while len(adjacency_list) != 2:
	for vertice in adjacency_list:
		if vertice != "0" and adjacency_list[vertice]["num"] == 0:
			Prufer_code.append(adjacency_list[vertice]["father"])
			adjacency_list[adjacency_list[vertice]["father"]]["num"] -= 1
			del adjacency_list[vertice]
			break	

print("Prufer code của dãy đã cho là:", " ".join(Prufer_code))