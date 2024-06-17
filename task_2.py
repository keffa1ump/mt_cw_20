import random

rand_lst = [random.randint(1, 20) for _ in range(1, 10)]

even_lst = [el for el in rand_lst if el % 2 == 0]
odd_lst = [el for el in rand_lst if el % 2 != 0]

print(even_lst, odd_lst, sep="\n")