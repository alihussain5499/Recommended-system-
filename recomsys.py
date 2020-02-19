# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 10:57:10 2019

@author: ali hussain
"""



f=open("D:/mystuff/friends.txt")
lines=f.readlines()[1:]
print(lines)


flist={}
for line in lines:
    w=line.strip().split(",")
    user=w[0]
    frnd=w[1]
    if flist.get(user)==None:
        flist[user]=[frnd]
    else:
        flist[user].append(frnd)
      
print(flist)

flists=[]
for line in lines:
    w=line.strip().split(",")
    u=w[0]
    f=w[1]
    flists.append([u,f])
    flists.append([f,u])
 
print(flists)    

friends={}
for line in flists:
    u=line[0]
    f=line[1]
    if friends.get(u)==None:
        friends[u]=[f]
    else:
        friends[u].append(f)

print(friends)

# Building Recommendation

def common(x,y):
    com=[]
    for v in x:
        if v in y:
            com.append(v)
            
    return com        


u=["ravi","swati","somu","sita"]
me=["ravi","devi","sita"]

common(u,me)

def recommend(x,y):
    rec=[]
    for v in x:
        if v not in y:
            rec.append(v)
    return rec

recommend(u,me)        

recommend(me,u)

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

out=open("D:/mystuff/fbreclist.txt","w")
hdr='"User"\t"people you may know "\n'
out.write(hdr)
for v in rec:
    rlist=rec[v]
    line=v+"\t"+",".join(rlist)+"\n"
    out.write(line)
    
out.close()    
    
    















