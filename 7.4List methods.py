#Here are some list methods:
'''append(x)---adds x to the end of the list
sort()---sorts(排序) the list
count(x)---returns the numbers of time x occurs in the list
index(x)---returns the location of the list occurrence of x
reverse()---reverses(使....反向) the list
remove(x)---removes first occurences of x in the list
pop(p)---removers the item at index p and return its value
insert(p,x)---inserts x at index p of the list'''
list1 =['Gogle','Runoob','Taobao']

list_pop=list1.pop(1)
print('删除的项为:',list_pop)
print('列表现在为:',list1)
print(list1.sort())

