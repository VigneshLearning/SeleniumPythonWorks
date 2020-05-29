my_tuple = ("Vignesh", "Divya", "Smrithi")
print(my_tuple)
print(my_tuple[2])

print(my_tuple[0:3])

for val in my_tuple:
    print(val)

my_tuple_2 = ("Amritha", (5,6,7), ["Austin","Hogan"])
print(my_tuple_2)
print(my_tuple_2[2][1])
my_tuple_2[2][1] = "Trish"
print(my_tuple_2)
print(my_tuple_2[2][1])

print("Amritha" in my_tuple_2)
print("Veena" in my_tuple_2)
