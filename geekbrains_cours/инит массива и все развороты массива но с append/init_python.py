arr = [2, 4, 5, 1, 7]
arr1 = [[0]*5]
arr1 = arr
print(arr1)

size = len(arr)

arr = [2, 4, 5, 1, 7]
arr1 = [[0]*size]
arr1 = arr
print(arr1)

arr = [2, 4, 5, 1, 7]
arr1 = [[0]*len(arr)]
arr1 = arr
print(arr1)

a = [2, 4, 5, 1, 7]
b = [[0]*len(a)]
i = a.index(4) # у значения 4 есть индекс => [1] => 4 
print (i) 

A = ["boy","girl","place","food"]
B = ["he","she","USA,UK","Pizza,Burger,Sushi"]
i = A.index('girl')
print (B[i])  # he


