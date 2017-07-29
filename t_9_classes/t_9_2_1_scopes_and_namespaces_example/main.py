def scope_test():
    def do_local():
        spam = "local spam"

    def do_non_local():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)

    do_non_local()
    print("After nonlocal assignment:", spam)

    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope", spam)
