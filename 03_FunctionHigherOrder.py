def greet():
    print("Hi")

x = 10
s1 = "Test"

print(type(x))
print(type(s1))
print(type(greet))

def Runner(obj):
    obj()

Runner(greet)