def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'yes', 'yep'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('Invalid user response')
        print(reminder)


ask_ok('Do you really want to quit ?')

i = 5


def f(arg=i):
    print(arg)

i = 6
print('Default value is other valuable scope:')
f()


def f(a, L=[]):
    L.append(a)
    return L

print('Default value is assigned only one time:', f(1))
print('Default value is assigned only one time:', f(2))
print('Default value is assigned only one time:', f(3))
