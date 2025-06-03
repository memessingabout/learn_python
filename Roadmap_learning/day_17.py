""" Day 17: Scope and Global vs Local Variables """

x = 5
def show():
    x = 10
    print(x)
show()
print(x)
