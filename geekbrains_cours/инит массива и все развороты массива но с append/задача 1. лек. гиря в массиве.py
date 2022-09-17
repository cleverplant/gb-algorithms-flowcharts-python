numbers = [1, 8, 3, 2, 6]
size = 5
index = 0
max = numbers[0]
min_ind = 0
while index < size:
    if numbers[index] > max:
       max =  numbers[index]
       max_ind = index
    index = index + 1
print('макс. вес гири: ' + str(max))
print('индекс(адрес) этой гири в массиве: ' + str(max_ind))       








