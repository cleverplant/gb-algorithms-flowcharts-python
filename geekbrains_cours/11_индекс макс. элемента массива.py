array = [1, 8, 3, 2, 6]
size = len(array)
index = 0
maxIndex = 0
max = array[0] # 'это мы задали то, что начало отсчета индекса максимального значения гири будет 0 т.е [0] 
while (index < size):
    if (array[index] > max):
        max = array[index]
        maxIndex = index
    index = index + 1
# print(max)        
# print(maxIndex)
second_max = array[0] # почему array[0], а не array[index] - ?
if (maxIndex == 0):
    second_max = array[1]
while (index < size):
    if (index != maxIndex):
        if (array[index] > second_max):
            second_max = array[index]
    index = index + 1
print(second_max)            







