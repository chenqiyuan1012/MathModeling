from networkx.algorithms.shortest_paths.generic import shortest_path
from networkx.algorithms.shortest_paths.weighted import dijkstra_path
import pandas as pd
import numpy as np
import networkx as nx


def GetResult(sc,tg):
    
    with open('data.txt','r',encoding='UTF-8') as f:
        lines=f.readlines()

    a=np.zeros([4000,4000])
    b=np.zeros([4000,4000])#b[i,j]表示从i到j的最短时间
    c=np.zeros([4000,4000])
    d=np.zeros([4000,4000])#花费矩阵
    e=np.zeros([4000,4000])#e[i,j]表示从i到j的站数
    G=nx.MultiDiGraph()


    def SplitAndReversed(list,flag=True):
        #if flag is false,reverse the list
        if not flag:
            return list[::-1]
        else:
            list=list.replace('上行：','')
            list=list.replace('下行：','')
            list=list.replace('环行：','')
            return list[:-1].split('-')
            
    def GetMatrix(list,num,price,target):
        l=len(list)
        #i，j表示是当前线路的第i，j个节点
        for i in range(l):
            start=list[i].replace('S','')
            for j in range(l): 
                end=list[j].replace('S','')
                if(end==target):flag=0
                else:flag=1
                if(start!=end):
                    a[int(start),int(end)]+=1
                    if(b[int(start),int(end)]==0 or 
                    abs((i-j)*3)<b[int(start),int(end)]):
                        b[int(start),int(end)]=abs((i-j)*3)+flag*5
                        c[int(start),int(end)]=num
                        d[int(start),int(end)]=GetPrice(price,abs(i-j))
                        e[int(start),int(end)]=abs(i-j)
                        G.add_edge(int(start),int(end),weight=GetPrice(price,abs(i-j)))
                        #print(G.get_edge_data(int(start),int(end)))
                    if(abs((i-j)*3)==b[int(start),int(end)]):
                        ls=[c[int(start),int(end)]]
                        ls.append(num)
                        c[int(start),int(end)]=ls

    def GetPrice(str,dis):
        if(str=='单一票制1元。' or dis<=20):
            return 1
        else:
            if(dis>=21 and dis<=40): return 2
            else: return 3

    for tmp in range(1,521):
        name=lines[(tmp-1)*4]
        price=lines[(tmp-1)*4+1]
        up=lines[(tmp-1)*4+2]
        """ if('环' not in up):
            up=SplitAndReversed(up)
            GetMatrix(up,tmp,price,tg)
            down=lines[(tmp-1)*4+3]
            if(len(down)>3):
                down=SplitAndReversed(lines[(tmp-1)*4+3])
            else:
                #如果没有下行，那么使用上行数据反转
                down=SplitAndReversed(up,flag=False)
            GetMatrix(down,tmp,price,tg)
        else:
            up=SplitAndReversed(up)
            GetMatrix(up,tmp,price,tg)
            down=lines[(tmp-1)*4+3] """
        up=SplitAndReversed(up)
        GetMatrix(up,tmp,price,tg)
        down=lines[(tmp-1)*4+3]
        if(len(down)>3):
            down=SplitAndReversed(lines[(tmp-1)*4+3])
        else:
            #如果没有下行，那么使用上行数据反转
            down=SplitAndReversed(up,flag=False)
        GetMatrix(down,tmp,price,tg)


    #sc=input('请输入起点：')
    #tg=input('请输入终点：')
    print('花费最小路径为：',nx.dijkstra_path(G,source=sc,target=tg))
    print('最小花费为：',nx.dijkstra_path_length(G,source=sc,target=tg))

    path=nx.dijkstra_path(G,source=sc,target=tg)
    l=len(path)
    cost=0
    car=[]
    wait=[]
    for i in range(l-1):
        cost+=d[path[i],path[i+1]]
        car.append(c[path[i],path[i+1]])
        wait.append(e[path[i],path[i+1]])

    print('花费为：',cost)
    print('车号为：',car)
    print('等待车站数量为：',wait)
    f.close()


    f.close()



scs=[3359,1557,971,8,148,87]
tgs=[1828,481,485,73,485,3676]

for i in range(6):
    print("第{}组的结果：".format(str(i)))
    GetResult(scs[i],tgs[i])