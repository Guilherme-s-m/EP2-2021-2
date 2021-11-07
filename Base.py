import random
def cria_pecas():
    pç=[[1,3],[0,1],[4,6],[0,3],[0,4],[6,6],[0,6],[1,1],[1,2],[0,0],[1,4],[1,5],[1,6],[2,2],[3,6],[2,4],[2,5],[2,6],[3,3],[3,4],[2,3],[3,5],[4,4],[4,5],[0,2],[5,5],[5,6],[0,5]]
    random.shuffle(pç)
    return pç
print(cria_pecas())
def inicia_jogo(a,b):
    if a==2:
        x={'jogadores':{0:[b[0],b[1],b[2],b[3],b[4],b[5],b[6]],1:[b[7],b[8],b[9],b[10],b[11],b[12],b[13]]},'monte':[b[14],b[15],b[16],b[17],b[18],b[19],b[20],b[21],b[22],b[23],b[24],b[25],b[26],b[27]],'mesa':[]}
    elif a==3:
        x={'jogadores':{0:[b[0],b[1],b[2],b[3],b[4],b[5],b[6]],1:[b[7],b[8],b[9],b[10],b[11],b[12],b[13]],2:[b[14],b[15],b[16],b[17],b[18],b[19],b[20]]},'monte':[b[21],b[22],b[23],b[24],b[25],b[26],b[27]],'mesa':[]}
    elif a==4:
        x={'jogadores':{0:[b[0],b[1],b[2],b[3],b[4],b[5],b[6]],1:[b[7],b[8],b[9],b[10],b[11],b[12],b[13]],2:[b[14],b[15],b[16],b[17],b[18],b[19],b[20]],3:[b[21],b[22],b[23],b[24],b[25],b[26],b[27]]},'monte':[],'mesa':[]}
    return x
def verifica_ganhador(a):
    x=8
    for i in range(len(a)):
        if a[i]==[]:
            x=i
    if x != 8:
        return x
    else:
        return -1
def soma_pecas(x):
    a=0
    for i in range(len(x)):
        for e in range(len(x[1])):
            a += x[i][e]
    return a
def posicoes_possiveis(x,y):
    a=[]
    o=0
    if x == []:
        return [0, 1, 2, 3, 4, 5, 6]
    for s in range(len(y)):
        o+=1
        for w in range(len(y[0])):
            if y[s][w]==x[0][0] or y[s][w]==x[-1][1]:
                a.append(o-1)
            if  len(a) > 2 and (a[len(a)-1] == a[len(a)-2]):
                del a[len(a)-1]
    return a
def adiciona_na_mesa(x,y):
    x1=[x[1],x[0]]
    if y==[]:
        y=x
    if x[0] == y[0][0]:
        y.insert(0,x1)
    elif x[1]== y[0][0]:
        y.insert(0,x)
    elif x[0]== y[-1][1]:
        y.append(x)
    elif x[1]== y[-1][1]:
        y.append(x1)
    return y

