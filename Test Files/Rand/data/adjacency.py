file1= open("fbs.txt")
n = 2016
m = 24000
a =[[0 for i in range(n)] for j in range(n)]

edges =[]
for i in range(m):
       edges.append(file1.readline().split(" "))
       edges[i].remove('\n')
       edges[i] = list(map(int, edges[i]))

# print(edges)

for i in range(len(edges)):
       a[edges[i][0]][edges[i][1]]=1
       a[edges[i][1]][edges[i][0]]=1

file1 = open("fbsecrets.txt", "w")

for i in range(len(a)):
       for j in range(len(a[i])):
              file1.write(str(a[i][j])+" ")
       file1.write("\n")
file1.close()
