import random
a = random.sample(range(0, 100), random.randint(1,25))
b = random.sample(range(0, 100), random.randint(1,25))
x = []

print(a)
print(b)

for ele in a:
    if ele in b:
        if ele not in x:
            x.append(ele)
print(x)
