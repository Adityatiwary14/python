def modify(x):
    x=15
    print(x,id(x))
x=10
modify(x)
print(x,id(x))

"""
output

15 1903102984880
10 1903102984720
"""