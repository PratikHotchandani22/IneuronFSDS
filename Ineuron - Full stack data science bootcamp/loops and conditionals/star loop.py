# n = 8
# for i in range(n,0,-1):
#     for j in range(i-1,0,-1):
#         print("+", end="")
#     print("\r")



def starLoop():
    n = int(input("Please enter how many rows"))
    for i in range(0,n+1):
        for j in range(i,n):
            print(end=" ")
        
        for j in range(i*2-1):
            print("*", end="")
        print("\r")


def starLoopWhile():
    n = int(input("Please enter number of rows"))
    i = 0
    j = i
    while i<n+1:
        while j < n:
            print(end=" ")
        
        while j < (i * 2) -1:
            print("*", end="")
        i = i + 1
        print("\r")




starLoopWhile()

