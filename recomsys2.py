# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 12:09:23 2019

@author: ali hussain
"""

f=open("D:/mystuff/friend.txt")
lines=f.readlines()[1:]
print(lines)

flist1={}
flist2={}
for line in lines:
    w=line.strip().split(",")
    user=w[0]
    f=w[1]
    if flist1.get(user)==None:
        flist1[user]=[f]
    else:
        flist1[user].append(f)
        
print(flist1)        

    
for line in lines:
    w=line.strip().split(",")
    f=w[1]
    ff=w[2]
    if flist2.get(f)==None:
        flist2[f]=[ff]
    else:
        flist2[f].append(ff)

print(flist2)

flist=[]
for line in lines:
    w=line.strip().split(",")
    u=w[0]
    f=w[1]
    ff=w[-1]
    flist.append([u,f])
    flist.append([f,u])
    flist.append([f,ff])
    flist.append([ff,f])
    flist.append([u,ff])
    flist.append([ff,u])

print(flist)    
    

friends={}
for line in flist:
    u=line[0]
    f=line[1]
    if friends.get(u)==None:
        friends[u]=[f]
    else:
        friends[u].append(f)

print(friends)

def common(x,y):
    com=[]
    for v in x:
        if v in y:
            com.append(v)
            
    return com        

i=["sita","ravi","devil","sanu","manu"]
u=["ravi","swati","somu","sita","manu"]
me=["ravi","devi","sita","somu"]


common(u,me)

common(i,u)

common(u,me)

def recommend(x,y):
    rec=[]
    for v in x:
        if v not in y:
            rec.append(v)
    return rec

recommend(u,me)        

recommend(me,u)

recommend(i,u)

recommend(u,i)

recommend(me,i)

recommend(i,me)


recs={}
for k in friends:
    rlist=[]
    kf=friends[k]
    for f in kf:
        rlist+=recommend(friends[f],kf)
        recs[k]=rlist

print(recs)        

rec={}
for k in friends:
    rlist=[]
    kf=friends[k]
    for f in kf:
        rlist+=recommend(friends[f],kf)
    fr=[v for v in rlist if v!=k]
    rec[k]=list(set(fr))
print(rec)    



out=open("D:/mystuff/fbrecommendlist.txt","w")
hdr='"User"\t"people you may know "\n'
out.write(hdr)
for v in rec:
    rlist=rec[v]
    line=v+"\t"+",".join(rlist)+"\n"
    out.write(line)
    
out.close()  









