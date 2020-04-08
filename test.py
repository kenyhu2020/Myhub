#a=12
#def change():
#    global a
#    print(a)
#    a=23
#print('Before the function call',a)
#print('inside change function',end=' ')
#change()
#print('After the function call',a)
#def test(a,b=-99):
#    if a>b:
#        return True
#    else:
#        return False
#result=test(12,56)
#print(result)

def high(l):
    return [i.upper() for i in l]

def test(h,l):
    return h(l)
l=['Python','Linux','Git']
print(test(high,l))
