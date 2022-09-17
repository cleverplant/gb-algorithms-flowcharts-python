print('''---инициализация массива & 
присвоение одного массива другому
''')
N = 5
a = [2, 4, 5, 1, 7]
b = [[0]*N] # <=== инициализация array
b = a  #      <=== операция присваивания не копирует объект, 
                 # он лишь создаёт ссылку на объект
print('массиву b =', b, 'присвоен a =', a )
print()
N = 5
a = [2, 4, 5, 1, 7]
b = [[0]*N]
b = a
index = b.index(5)
print(index)
print()
N = 5
a = [2, 4, 5, 1, 7]
b = [[0]*N]
b = a
ind = b.index(5)
print(ind)
print()
print('---цикл while---\n')
N = 5
i = 0
while i < N:
    print('Цикл выполняется', i, 'раз(а)')
    i = i + 1
print('Цикл окончен')
print('Цикл выполнился', i, 'раз(а)\n')  

print('---цикл while & if---\n')
N = 5
i = 0
while i < N:
   if N == 5:
      print('Цикл выполняется', i, 'раз(а)')
   i = i + 1
print('Цикл окончен')
print('Цикл выполнился', i, 'раз(а)\n')    

a = [2, 4, 5, 1, 7]
b = []
i = len(a) - 1
while i >= 0:
    tmp = a[i]
    b.append(tmp)
    i = i - 1
print(b)  # [ 7, 1, 5, 4, 2]
print()

a = [2, 4, 5, 1, 7]
b = []
i = 0
s = len(a) - 1
while i < len(a):
    b[s] = a[i] 
    s = s - 1
    i = i + 1
    
print(b)  # [ 7, 1, 5, 4, 2]
print()



'''
N = 5
a = [2, 4, 5, 1, 7]
b = []
i = 0
while i < N:
   tmp = a[i]
   b.append(tmp)
   i = i + 1
print(b)
'''



