'''
a = [1, 2, 3] # >>>print(a) -> [1, 2, 3]
a is a #print(a is a) con la lista anterior -> True
a + [] is a #print(a + [] is a) -> False
a + [] == a #print(a + [] == a) -> True
[10, 20, 3] > [1, 2, 3] #True
[10, 2, 3] > [1, 2, 3] #True­
[1, 20, 30] > [1, 2, 3]­ #True
[0, 2, 3] <= [1, 2, 3] #False­
[1] < [2, 3] #True­
[1] < [1, 2] #True
[1, 2] < [0] #False
a = list(range(1, 4)) #print(a) -> [1, 2, 3]
[1, 2] == [1, 2] #True
[1, 2] is [1, 2] #True

a = [1, 2, 3]
b = [a[0], a[1], a[2]] #Almaceno en esos indices dichos valores de a
print(a == b) #True
print(a is b) #False
print(a[0] == b[1]) #False
 b is [b[0], b[1], b[2]] #True
'''