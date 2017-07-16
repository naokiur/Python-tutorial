baskets = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(baskets)

print('orange' in baskets)
print('crabgrass' in baskets)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

c = {x for x in 'abracadabra' if x not in 'abc'}
print(c)
