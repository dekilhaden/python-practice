x = 10
ptr =id(x)
print(ptr)
x = 15
print(id(x))

string = "Geeks"

def test(string):
    string = "GeeksforGeeks"
    print("Inside Function", string)

test(string)
print("Outside Function", string)