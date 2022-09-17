count = 0
distanse = 10000
firstFriendSpeed = 1
secondFriendSpeed = 2
dogSpeed = 5
friend = 2 # это флаг. он задает направление движения собаки (ко второму другу)

while (distanse > 10):
    if friend == 1:
        time = distanse / (firstFriendSpeed + dogSpeed)
        friend = 2
    else:
        time = distanse / (secondFriendSpeed + dogSpeed)
        friend = 1
    distanse = distanse - ( (firstFriendSpeed + secondFriendSpeed) * time )
    count = count + 1
print(count)    
print('собака пробежит: ' + str(count) + ' раз')    