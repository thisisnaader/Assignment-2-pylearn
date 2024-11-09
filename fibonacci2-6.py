n = int(input())

n1 = 0
n2 = 1
count = 1
nextnum = n2

if n == 1:
    print("0") 
elif n == 2:
    print("0 1") 
elif n > 2 :
    print(n1, n2,end=" ")
    while count <= n-2:
     nextnum = n1 + n2
     print(nextnum,end=" ")
     n1, n2 =n2, nextnum
     count += 1
     

