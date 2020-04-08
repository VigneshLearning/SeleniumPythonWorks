x = 5
y = 7
t = x + y

print(t)

if 10 > 5:
    print("c")

def add(a,b):
    print(a+b)

x = add(20,30)

x = 3
y = 9.7
z = 8,0

print(type(x))
print(type(y))
print(type(z))

# Casting

x = int(2)
y = int(3.6)
d = float(5)
f = str(7)

print(x)
print(y)
print(d)
print(f)
print(x+y)
print(y+d)

# String functions

x = "Hello Undertaker..."
print(x[9:17])
print(len(x))
print(x.lower())
print(x.upper())

x = "    Hello Undertaker...   "
print(x[9:17])
print(len(x))
print(x.lower())
print(x.upper())
print(x)
print(x.strip())
print(x.replace("e",""))
print(x.replace("e","a"))
print(x)
print(x.split("."))

# Input Functions

print("Ingresar tu nombre : ")
x = input()
y = "bienvenido"
print(y.upper() + " " + x.upper())
