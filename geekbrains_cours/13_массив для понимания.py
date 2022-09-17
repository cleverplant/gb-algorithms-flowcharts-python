numbers = [1, 8, 3, 2, 6]
size = 5
current_index = 0 # current_index - текущий индекс тупо - i = i + 1
max_numbers_index = 0 # max_numbers_index - место - индекс max значания ( гиря 8кг[index] ), где в массиве находится самая тяжелая гиря
max = numbers[0]
while (current_index < size):
    if (numbers[current_index] > max):
        max = numbers[current_index]
        max_numbers_index = current_index 
    current_index = current_index + 1
current_index = 0
second_max = numbers[0] # почему
if (max_numbers_index == 0):
    second_max = numbers[1]
while (current_index < size):
    if (current_index != max_numbers_index):
        if (numbers[current_index] > second_max):
            second_max = numbers[current_index]
    current_index = current_index + 1
print(second_max)  # второе по значению макс. величина гири = 6кг     
print(max) # ьфкс. значение величины гири = 8кг
print(max_numbers_index) # индекс максимального значения величины гири = место(адрес) в массиве
print(current_index) # текущее значение счетчик

print('================================================= \n')

numbers = [1, 8, 3, 2, 6]
size = 5
current_index = 0 # current_index - текущий индекс тупо - i = i + 1
max_numbers_index = 0 # max_numbers_index - место - индекс max значания ( гиря 8кг[index] ), где в массиве находится самая тяжелая гиря
max = numbers[0]
while (current_index < size):
    if (numbers[current_index] > max):
        max = numbers[current_index]
        max_numbers_index = current_index 
    current_index = current_index + 1
current_index = 0
second_max = numbers[0] # почему
if (max_numbers_index == 0):
    second_max = numbers[1]
while (current_index < size):
    if (current_index != max_numbers_index):
        if (numbers[current_index] > second_max):
            second_max = numbers[current_index]
    current_index = current_index + 1
print(second_max)  # второе по значению макс. величина гири = 6кг     
print(max) # ьфкс. значение величины гири = 8кг
print(max_numbers_index) # индекс максимального значения величины гири = место(адрес) в массиве
print(current_index) # текущее значение счетчик

print('================================================= \n')

# ЗАДАЧА
         
# Найти второе максимальное число 
# (имеется ввиду не вес гири а адрес в массиве - не 6кг, а где она в массиве )
# это решение на исключение индекса, а можно было просто отнять от индекса макс. единицу в конце программы
# фиксируем не только его величину (значение), а и место - его индекс, где в массиве он находится