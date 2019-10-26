import math


k=0
data=[]
centroid=[]
cluster=[]



def findcent(x):
   
    for j in range(1,len(data[0])):
        b=0
        for i in cluster[x]:
            b = b + data[i-1][j]
        centroid[x][j-1]=b/len(cluster[x])
    


def dist(a,b):
    x=0
    for i in range(len(a)):
        x=x+(a[i]-b[i])**2
    return(math.sqrt(x))
    
    

def printclus():
    for i in range(k):
       # print(cluster[i],end='\t')
       # print(centroid[i],end='  ')
        print(len(cluster[i]),end='\t')
       
        
        
        
#open file 
f=open("data4.txt","r")
contents=f.read()
data=contents.split("\n")

for i in range(len(data)):
    data[i]=data[i].split()
    data[i]=[float(j) for j in data[i]]
    data[i][0]=int(data[i][0])
k=int(input('enter no of clusters: '))


for i in range(k):
#for i in [0,1,6]:
    centroid.append(data[i][1:])
    cluster.append([data[i][0]])


for i in range(k,len(data)):
    min=dist(centroid[0],data[i][1:])
    clus=0
    for j in range(1,k):
        d=dist(centroid[j],data[i][1:])
        if(min>d):
            min=d
            clus=j
    cluster[clus].append(i+1)       
    findcent(j)
    

printclus()


while 2>1:
    flag=0
    for i in range(k):
        for a in cluster[i]:
            min=dist(centroid[0],data[a-1][1:])
            clus=i
            
            #find min dist
            for j in range(1,k):
                d=dist(centroid[j],data[a-1][1:])
                if(min>d):
                   # print('a=',a,' clus=',j,end='\n')
                    min=d
                    clus=j           
            #if new cluster found
            if(clus!=i):
                #print(i,'->',a,'->',j,end='\t')#
                cluster[i].remove(a)
                findcent(i)
                cluster[clus].append(a)
                findcent(clus)
                flag=1
                printclus()#
                print()#
               
            
    
    #print('flag check:',flag)
    if (flag==0):
        break;
        
  
print('\n\nfinal')
printclus()






'''
DATASET

1   2   2
2   1   14
3   10  7
4   1   11
5   3   4
6   11  8
7   4   3
8   12  9

'''





























