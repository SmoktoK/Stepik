# На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая создает из указанных чисел список, затем удаляет все элементы стоящие по нечетным индексам,
# а затем выводит полученный список.

n = int(input())
my_list = []
new_list = []
for i in range(n):
    x = int(input())
    my_list.append(x)
for i in range(n):
    if i % 2 == 0:
        new_list.append(my_list[i])

print(new_list)