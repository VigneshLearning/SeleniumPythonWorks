a = 5
b = 5
if a>b:
    print("this is false")
elif a<b:
    print("this is true")
else:
    print("What the fuck")


# For Loop

num = [1,2,3,4,5]
sum = 0
for val in num:
    sum=sum+val
    print(sum)

players = ["Batista", "Kane", "Stone Cold"]
for val in players:
    print(val)
else:
    print("Nothing is there")

# While functions

print("Enter any value :")
num = int(input())
# num = 5
sum = 0
i = 1

while i<num:
    sum=sum+i
    i=i+1
print("Total value is", i)