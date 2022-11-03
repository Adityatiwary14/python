#filter fruits which carry a and e
fruits = ["apple","cherry","banana","guava"]
fruit = [i for i in fruits if 'a' in i and 'e' in i]
print("fruits containing 'a' and 'e' are : ",fruit)