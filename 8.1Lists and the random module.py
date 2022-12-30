#choice(L)#picks a random item from L
#sample(L,n)#picks a group of n random items from L
#shuffle(L)#Shuffles(随机排列) the items of L,这会modifies the original list,
'''如果不想change list,造个复制的'''

from random import choice,sample,shuffle
names = ['ZhangXiang','Zhou Jiaxing','Zhang Chong','Liu Xing']
current_player =choice(names)             #1
team =sample(names,4)                     #2
print(team)
print(current_player)
print('\n\n')
#choice也可用于string，来刷个屏
s='qwertyuiopasdfghjklzxcvbnm!@#$%^&*()'
for i in range(500):
    print(choice(s),end='')               #3
print('\n\n')
#Here is a nice use of shuffle to pick a random ordering of players in a game
for p in names:                           #4
    print(p,'it is your turn.')
    # code to play the game goes here...
shuffle(names)
teams =[]
for i in range(0,len(names),2):
    teams.append([names[i],names[i+1]])
print(teams)

