#coding:gbk
"""
人物关系
作者:黄玉坤
"""
import jieba
import jieba.posseg as pos
import codecs

names={}        #引入人名
relation={}#引入人物关系
Names=[]
jieba.load_userdict("names.txt")#导入人物
with open("黎明破晓的街道.txt",encoding="gbk","r") as novel:
    for line in novel.readlines():
        poss=pos.cut(line)  
        Names.append([])  
        for X in poss:
            if X.flag!='nr' or len(X.word)<2:
                continue
            Names[-1].append(X.word) 
            if names.get(X.word) is None: 
                names[X.word]=0
                relation[X.word]={}
            names[X.word]+=1 

for N in Names:
    for N1 in N:
        for N2 in N:
            if N1==N2:
                continue
            if relation[N1].get(N2) is None:
                relation[N1][N2]=1
            else:
                relation[N1][N2] = relation[N1][N2]+1
with codecs.open("People1.csv","gbk","X") as P:
    P.write("1,2,3\n")
    for name, times in names.items():
        if times>10:
            P.write(name+","+name+","+str(times)+"\n")
with codecs.open("People2.csv", "X", "gbk") as P:
    P.write("1,2,3\n")
    for name,edges in relation.items():
        for v,X in edges.items():
            if X > 10:
                P.write(name+","+v+","+str(X)+"\n")
