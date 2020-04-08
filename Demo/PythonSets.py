my_set = {"Mate", "Yerba", "Bombilla"}
print(my_set)

#print(my_set[2]) - Not Possible

#print(my_set[0:3]) - Not Possible

for val in my_set:
    print(val)

print("Mate" in my_set)
print("Mates" in my_set)

my_set.add("Canarias")
print(my_set)
my_set.update(["Cabreal","Sara","JenGibre"])
print(my_set)

my_set.discard("JenGibre")
print(my_set)
my_set.discard("JenGibre")
print(my_set)



my_list = [1,2,3]
print(my_list)
my_set_2 = set(my_list)
print(my_set_2)

A = {'A','B','C', 1, 3, 5}
B = {'C','A','D', 2, 1, 4}
print(A.union(B))
print(A.intersection(B))

print(A | B)
print(A & B)

print(A.difference(B))
print(B.difference(A))
print(A - B)
print(B - A)

print(A.symmetric_difference(B))
print(B.symmetric_difference(A))
print(A ^ B)
print(B ^ A)

print("Go Ahead, You are already half way on this Course.")