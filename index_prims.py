INF = 9999999

Nv = 5

G = [[0, 4, 2, 0, 0],
     [0, 0, 3, 2, 3],
     [0, 1, 0, 4, 5],
     [0, 0, 0, 0, 0],
     [0, 0, 0, -5, 0]]

selected_node = [0, 0, 0, 0, 0]

no_edge = 0

selected_node[0] = True


print("Edge : Weight\n")
while (no_edge < Nv - 1):
    
    minimum = INF
    a = 0
    b = 0
    for m in range(Nv):
        if selected_node[m]:
            for n in range(Nv):
                if ((not selected_node[n]) and G[m][n]):  
                    
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    selected_node[b] = True
    no_edge += 1
