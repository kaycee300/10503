DataSet={0:[4, 21, 'A'],
         1:[5, 19, 'A'],
         2:[10, 24, 'B'],
         3:[4, 17, 'A'],
         4:[3, 16, 'A'],
         5:[11, 25, 'B'],
         6:[14, 24, 'B'],
         7:[8, 22, 'A'],
         8:[10, 21, 'B'],
         9:[12, 21, 'B'],
         }

x=9
y=21
k=3

distances=[]
order=[]
result=[]

def sorting(z):
    t=[]
    for y in z:
        t.append(y)
    for i in range(len(t)-1):
        
        for i in range(len(t)-1):
            if t[i]>t[i+1]:
                bigger=t[i]
                t[i]=t[i+1]
                t[i+1]=bigger
        
    return t

def euclideanDistance(height, width, x, y):
    return ((x-height)**2+(y-width)**2)**0.5


def kNearestNeighbor():
    for i in range(len(DataSet)):
        distances.append(euclideanDistance(DataSet[i][0], DataSet[i][1], x, y))
    return distances

def selecting(kk, kdistances, korder):
    result=[]
    for h in range(kk):
        for q in range(len(kdistances)):
            if(korder[h]==kdistances[q]):
                result.append(q)
    return result


def voting(select, DataSet):
    A=0
    B=0
    
    for j in select:
        if(DataSet[j][2]=='A'):
            A=A+1
        elif(DataSet[j][2]=='B'):
            B=B+1
        
    if A>B:
        print('New sample is A')
    elif B>A:
        print('New sample is B')
    print(A,'A')
    print(B,'B')

distances=kNearestNeighbor()
print('distances: ',distances)
print()

order=sorting(distances)
print('order: ', order)
print()

select=selecting(k, distances, order)

print('select: ', select)
print()

voting(select, DataSet)
print()