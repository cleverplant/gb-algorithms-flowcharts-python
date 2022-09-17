print('---УЧИТЕЛЬ 1--------------------')  
N = 7
arr = [1, 2, 3, 4, 5, 6, 7]
i = 0
while (i < N/2):
    tmp = arr[(N - 1) - i] 
    tmp = arr[i]
    #arr[(N - 1) - i] = arr[i]
    arr[ i ] = tmp 
    i = i + 1
print(arr)
print('---УЧИТЕЛЬ 2---------------------') 

arr = [1, 2, 3, 4, 5, 6, 7]
size = len(arr)
last = (size - 1)
number = last
arr_1 = []
i = 0
while (i <= last):
    print(number)
    number = number - 1
    i = i + 1 
print('size: ' + str(size)) 
print('last: ' + str(last)) 
print('arr: ' + str(number + 1))

'''

print('---ЧЕРНОВИК_1---------------------') 
array = [2, 5, 13, 7, 6, 4]
size = len(array) 
i = size - 1
while i > 0:
    array[i]
    i = i - 1
print(array)    

print('---ЧЕРНОВИК_2---------------------')

array = [2, 5, 13, 7, 6, 4]
size = len(array)
i = 0
number = (size - 1)
while i < size/2: # <= 
    array[number]
    number = number - 1
    i = i + 1
print(array)
'''
