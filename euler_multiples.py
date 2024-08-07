multiples_list: list = []

for i in range(1000):
    if (i%3==0) or (i%5==0):
        multiples_list.append(i)

multiples_sum: int = sum(multiples_list)
print(multiples_sum)