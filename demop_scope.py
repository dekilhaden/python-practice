def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
        myinnerfunc()

myfunc()

x = 300

def myfunc():
    print("Inside Function", x)

myfunc()

print("Outside Function",x)
print(24,x)

def func(): #keyword
    global x  = 300

myfunc()
print(x)
