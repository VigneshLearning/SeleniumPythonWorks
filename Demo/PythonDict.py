my_dict = {
    "class" : "animal",
    "name" : "Elephant",
    "Age" : 12,
    "Place" : "Madurai"
}
print(my_dict)
print(my_dict["name"])
print(my_dict.get("name"))
print(my_dict.values())

for x in my_dict:
    #print(x)
    print(my_dict[x])

for x,y in my_dict.items():
    print(x,y)

my_dict["name"] = "Lion"
print(my_dict)
my_dict["sex"] = "male"
print(my_dict)
my_dict.pop("Age")
print(my_dict)

#del my_dict