# stats.py


def median(L):
    L.sort()
    print(L)
    a=L.count(L)
    if a % 2 ==0:
        x=(L[a/2]+L[(a/2)+1])/2
        print (x)
    else:
        x=(L[(a+1)/2])
        print (x)
L=[1,2,3,4,5,6,7,8,9,10,12,11,15,34,6,3,5,6,6]

median(L)

# def mode(L):
#     d={}
    
#     for i in L:
#         if i not in d:
#             d[i]=1
#         else:
#             d[i]+=1
    
#     return max(d)
    
# def mean(L):
#     a=sum(L)
#     avr=a/len(L)
#     return avr
    