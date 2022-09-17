print('---УЧИТЕЛЬ 1--------------------')  
N = 7
arr = [1, 2, 3, 4, 5, 6, 7]
i = 0
while (i < N/2):
    tmp = arr[(N - 1) - i ]
    arr[(N - 1) - i ] = arr[ i ]
    arr[ i ] = tmp
    i = i + 1 
print(arr)

print('--РАЗВОРОТ------') 

N = 7
arr = [1, 2, 3, 4, 5, 6, 7]
arr_2 = [] # [[0]*N]
i_2 = N - 1
i = 0

while (i < N):
   arr_2[i_2] = arr[i]
   i = i + 1

print(arr_2)





print('--КОПИРОВАНИЕ------') 

arr = [1, 2, 3, 4, 5, 6, 7]
N = 7
arr1 = [[0]*N]
arr2 = [[0]*N]
n = 0
i = 0
while (i < N):
    arr[i]
    arr2[[i]*N] = arr[i]
    i = i + 1
print(arr)
print(arr1)  
print(arr2)  

print('--РАЗВОРОТ------') 



