def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("it's", state, "!")

print("# 1 positional argument:")
parrot(1000)

print("# 1 keyword argument:")
parrot(voltage=1000)

print("# 2 keyword arguments")
parrot(voltage=1000000, action='VOOOOOOM')

print("# 2 keyword arguments")
parrot(action='VOOOOOOOM', voltage=1000000)

print("# 3 positional arguments")
parrot('a million', 'bereft of life', 'jump')

print("# 1 positional, 1 keyword")
parrot('a thousand', state='pushing up the daisies')

print("# required argument missing:", "parrot()")
print("# non-keyword argument after a keyword argument:", "parrot(voltage=5.0, 'dead')")
print("# duplicate value for the same argument:", "parrot(110, voltage=200)")
print("# unknown keyword argument:", "parrot(actor='John Cleese)")


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)

    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger",
           "It's very runny, sir.", "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
