print("normal call 'list(range(3, 6))' : ", list(range(3, 6)))
args = [3, 6]
print("call with unpacking argument 'list(range(*args))' : ", list(range(*args)))


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end='')
    print("if you put", voltage, "volts through it.", end='')
    print("E's", state, "!")


d = {
    "voltage": "four million",
    "state": "bleedin' demised",
    "action": "VOOM"
}
parrot(**d)
