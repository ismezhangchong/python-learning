words=['wdqoz','e','c','e','z',',/f[z']
#这是一个bug
'''for w in words:
    if w[4]=='z':
        print(w)
#'''
#改成这样
for w in words:
    if len(w)>=5 and w[4]=='z':
        print(w)

#Note
'''It might seem like we would still get an error because we are still checking w[4],
'''
#but there is no error. The key to why this works is short-circuiting.
#Python starts by checking the first part of the condition, len(w)>=5.
'''If that condition turns out to be false, then the whole and condition is
guaranteed to be false,
'''
#and so there is no point in even looking at the second condition. So Python
'''doesn’t bother with the second condition. You can rely on this behavior

Short-circuiting also happens with or conditions. In this case, Python checks the first part of the or
'''
#and if it is true, then the whole or is guaranteed to be true, and so Python will not bother checking
'''the second part of the or'''
