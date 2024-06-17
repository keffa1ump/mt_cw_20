from functools import reduce

num = input("Введите числа через пробел: ")

lst_1 = [int(el) for el in num.split()]

sum_lambda = lambda lst : sum(lst)
print(sum_lambda(lst_1))

mult_lambda = reduce((lambda x,y : x*y), lst_1)
print(mult_lambda)