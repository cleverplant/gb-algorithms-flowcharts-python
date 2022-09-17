# Задача 2. Напишите псевдокод по блок-схеме
# Найти среднее арифметическое среди всех элементов массива [2, 5, 13, 7, 6, 4]

numbers = [2, 5, 13, 7, 6, 4]
size = len(numbers) # определяем длину массива (унифицируем ПО )
sum = 0
arg = 0
index = 0
while (index < size):
    sum = sum + numbers[index]
    index = index + 1
avg = sum / size
print(avg)  
print('ср.ариф.элементов массива: '+ str(avg))   
