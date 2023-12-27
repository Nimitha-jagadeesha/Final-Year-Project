# 0 Nimitha N0={Lp,Pappu,usa,Niriksha,sus,yasa}, P0 ={3/10,0,0,0,0,0}, S0= {DOB, Salary, Address}, Q0={0.1,0.7,0.5}
# 1 Lp N1={Nim,Lavanya,kavya,nayana,usa,sus,yasa}, P1 ={3/10, 0,0,0,0,0,0} S1={DOB, ph.No, Salary}, Q1={0.22,0.81,0.47}
# 2 Pappu {Salary}  
# 3 Usha
# 4 Sus
# 5 yasa
# 6 kavya
# 7 Niriksha
# 8 nayana
# 9 Lavanya

# P = 3/10
n = 2015
m = 2015
edges =[]
file1 = open("data/fbedges.txt")
for i in range(n):
       edges.append(file1.readline().split(" "))
       edges[i].remove("\n")
       edges[i] = list(map(int, edges[i]))
# print(edges)

N = [[] for i in range(n)]
for i in range(n):
       for j in range(n):
              if edges[i][j]==1 and i!=j:
                     N[i].append(j)
# print(N)

file1 = open("FbInitial.edges", "w")

for i in range(len(N)):
       for j in range(len(N[i])):
              file1.write(str(i)+" "+str(j)+"\n")
file1.close()
             
privacy =[]
file1 = open("data/fbprivacy.txt")
for i in range(n):
       privacy.append(file1.readline().split(" "))
       privacy[i]=privacy[i][0:-1] 
       privacy[i] = list(map(float, privacy[i]))
# print(privacy)

P = [[] for i in range(n)]
for i in range(n):
       for j in range(n):
              if edges[i][j]==1 and i!=j:
                     P[i].append(privacy[i][j])
# print(P)


secrets =[]
file1 = open("data/fbsecrets.txt")
for i in range(n):
       secrets.append(file1.readline().split(" "))
       secrets[i].remove("\n")
       secrets[i] = list(map(int, secrets[i]))
# print(secrets)

S = [[] for i in range(n)]
for i in range(n):
       for j in range(m):
              if secrets[i][j]==1:
                     S[i].append(j)
# print(S)


thresholdlist =[]
file1 = open("data/fbthershold.txt")
for i in range(n):
       thresholdlist.append(file1.readline().split(" "))
       thresholdlist[i]=thresholdlist[i][0:-1] 
       thresholdlist[i] = list(map(float, thresholdlist[i]))
# print(thresholdlist)

Q = [[] for i in range(n)]
for i in range(n):
       for j in range(m):
              if secrets[i][j]==1:
                     Q[i].append(thresholdlist[i][j])
                     if(Q[i][-1]==0):
                            Q[i][-1]=0.1
# print(Q)

C = [i for i in range(n)]
Sel =set()
Pmax = 0
l = [i for i in range(n)]
while(len(l)):
       Rmax = -1
       s=-1 
       Wsel={}
       w=[0 for i in range(m)]
       for i in l:
              for j in range(m):
                     X = [val for val in C if(val in N[i])]
                     if(len(X)):
                            sec=S[X[0]]
                     else:
                            sec = []
                     for val  in X:
                            sec=[v for v in sec if v in S[val]]
                     # print("--------------------------------------------------------------------",i,j)
                     # print(sec)
                     # print("--------------------------------------------------------------------")
                     numerator=len(sec)
                     if len(X):
                            w[j]=numerator/len(X)
                     else:
                            w[j]=0
              S1 = sum([w[j]/Q[i][j] for j in range(len(Q[i]))])
              if S1 ==0:
                     R=0
              else:
                     R=sum(P[i])/S1
              if R>Rmax:
                     s=i
                     Rmax=R
                     Wsel=w 
              flag=True
              for j in range(len(Q[s])):
                     if Wsel[j]>Q[s][j]:
                            flag=False
                            break 
              if flag:
                     Sel.add(s)
                     C=[val for val in C if val in N[s]]
                     Pmax+=sum(P[s]) 
              if(s in l):
                     l.remove(s) 
print(Pmax,Sel)
OutputList =  [[] for i in range(n)]
for i in Sel:
       OutputList[i] = N[i]

file1 = open("Fboutput.edges", "w")

for i in range(len(OutputList)):
       for j in range(len(OutputList[i])):
              file1.write(str(i)+" "+str(j)+"\n")
file1.close()
print(OutputList)